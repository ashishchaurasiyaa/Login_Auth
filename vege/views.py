from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe
from .forms import ReceipeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login_page/')
def receipe(request):
    if request.method == "POST":
        form = ReceipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('receipe')

    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))


    form = ReceipeForm()
    context = {'receipes': queryset, 'form': form}
    return render(request, "receipe.html", context)

def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)

    if request.method == "POST":
        form = ReceipeForm(request.POST, request.FILES, instance=receipe)
        if form.is_valid():
            form.save()
            return redirect('receipe')

    form = ReceipeForm(instance=receipe)
    context = {'receipe': receipe, 'form': form}
    return render(request, 'update_receipe.html', context)

def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    return redirect('receipe')

def login_page(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invaild Username")
            return redirect('/login_page/')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,'Invaild Password')
            return redirect('/login_page/')
        else:
            login(user)
            return redirect('/login_page/')

    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def registration_page(request):
    if request.method =="POST":
        first_name =request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user =  User.objects.filter(username = username)
        if user.exists():
            messages.info(request,"Username allready taken")
            return redirect('/registration_page/')


        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.info(request,"Account created Successfully ")

        return redirect('/registration_page/')
    return render(request,"register.html")
