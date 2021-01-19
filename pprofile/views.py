from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, UserForm
from home.models import District

districts = District.objects.all()

# Create your views here.
@login_required
def profile(request):
    user = request.user
    context = {'user':user,'districts':districts}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    profile = user.profile
    # profile form
    pform = ProfileForm(instance=profile)
    # user form
    uform = UserForm(instance=user)

    if request.method == "POST":
        uform = UserForm(request.POST,instance=user)
        pform = ProfileForm(request.POST,request.FILES,instance=profile)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
            return redirect('profile')


    context = {'pform':pform,'uform':uform,'districts':districts}
    return render(request, 'edit_profile.html', context)

@login_required
def liked(request):
    return render(request,'liked.html',{'districts':districts})

@login_required
def saved(request):
    return render(request,'saved.html',{'districts':districts})

@login_required
def published(request):
    return render(request,'published.html',{'districts':districts})