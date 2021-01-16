from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group

from .forms import CreateUserForm
from pprofile.models import Profile

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']


            # log in the user as soon as registered
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')

    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'registration/register.html',context)

# because we use django's login, we do not need to re-implement this
# def login(request):
#     if request.method == "POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.info(request, 'username or password is incorrect')


    # context = {}
    # return render(request, 'registration/login.html')
