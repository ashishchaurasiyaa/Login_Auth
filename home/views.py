from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples =[
        {'name':'Ashish Chaurasiya','age':25},
        {'name':'Aman Saxena', 'age' : 24},
        {'name':'Gaurav Awad', 'age' : 22},
        {'name':'Karan Chaudhary', 'age': 24},
        {'name':'Abhishek', 'age':17}
    ]

    vegetables = ['Pumpkin','Tomato','Potatoe']
    return render(request, "home/index.html", context={'page':'Django 2023 Revision'  ,'people': peoples,'vegetable':vegetables})

def about(request):
    context ={'page':'About'}
    return render(request,"home/about.html",context)

def contact(request):
    context ={'page':'Contact'}
    return render(request,"home/contact.html",context)

def success_page(request):
    return HttpResponse("Nothing I'm Serious")
