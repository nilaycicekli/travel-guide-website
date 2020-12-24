from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def search_result(request):
    return render(request,'search_result.html')

def profile(request):
    return render(request,'profile.html')

def edit_profile(request):
    return render(request,'edit_profile.html')

def content(request):
    return render(request,'content.html')

def liked(request):
    return render(request,'liked.html')
    
def saved(request):
    return render(request,'saved.html')

def add_content(request):
    return render(request,'add_content.html')





