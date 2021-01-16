from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContentForm
from .models import Content

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def search_result(request):
    return render(request,'search_result.html')


def content(request, id):
    content = get_object_or_404(Content, id=id)
    # form = CommentForm()
    # tags_queryset = content.tag.all()
    # tags = [i for i in tags_queryset]
    
    return render(request,'content.html',{"content":content})


@login_required
def add_content(request):
    user = request.user
    if request.method == "POST":
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.author = user
            content.save()
            content.tag.set(form.cleaned_data['tag'])
            # return redirect('content', id=content.id)
            return redirect('content')
    else:
        form = ContentForm()
    return render(request,'add_content.html',{'form':form})






