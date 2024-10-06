from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")
def home(request):
    return render(request,'webapp/home.html')
def about(request):
    return render(request,'webapp/about.html')

def contact(request):
    return render(request,'webapp/contact.html')

def explore(request):
    context={}
    return render(request,'webapp/explore.html',context=context)