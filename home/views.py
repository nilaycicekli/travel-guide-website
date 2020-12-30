from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def search_result(request):
    return render(request,'search_result.html')

def content(request):
    return render(request,'content.html')

@login_required
def add_content(request):
    return render(request,'add_content.html')





