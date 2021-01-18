from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContentForm, CommentForm
from .models import Content, District, Comment, Tag
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
class SearchResultsView(ListView):
    model = Content
    template_name = 'search_result.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Content.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

        return object_list

def index(request):
  
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

#def search_result(request):
#   return render(request,'search_result.html')


def content(request, id):
    content = get_object_or_404(Content, id=id)
    form = CommentForm()
   # myFilter=ContentFilter(request.GET, queryset=content)
    return render(request,'content.html',{"content":content,"form":form})



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
            return redirect('content', id=content.id)
    else:
        form = ContentForm()
    return render(request,'add_content.html',{'form':form})

@login_required
def delete_content(request,id):
    content = get_object_or_404(Content, id=id)
    if request.user == content.author:
        content.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# #Like
# @login_required
# def like(request,id):
#     user = request.user
#     content = get_object_or_404(Content, id=id)
    
#     if not content.likes.filter(by=user,content=content):
#         like = Like(content=content,by = user)
#         like.save()
#     else:
#         like = get_object_or_404(Like,by=user, content=content)
#         like.delete()

#     return redirect('content', id=id)

#Like/Unlike 
@login_required
def like(request,id):
    user = request.user
    content = get_object_or_404(Content, id=id)

    if user not in content.likelist.all():
        content.likelist.add(user)

    else:
       content.likelist.remove(user)

    # return redirect('content', id=id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Save / Discard
@login_required
def save(request,id):
    user = request.user
    content = get_object_or_404(Content, id=id)

    if user not in content.savelist.all():
        content.savelist.add(user)

    else:
        content.savelist.remove(user)

    # return redirect('content', id=id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#Add Comment
@login_required
def add_comment(request,id):
    user=request.user
    content = get_object_or_404(Content, id=id)
    if request.method=="POST":
        
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.content = content
            comment.user=user
            comment.save()
            return redirect("content",id=content.id)
    else:
        form=CommentForm()
    return render(request,'content.html',{'form':form,'content':content})



#Remove Comment
@login_required
def remove_comment(request,id):
    user=request.user
    comment=get_object_or_404(Comment,id=id)
    if user==comment.user:
        comment.delete()
    return redirect("content",id=comment.content.id)


def district(request, id):
    try:
        district = get_object_or_404(District, id=id)
        result = district.content.all()
        return render(request,'search_result.html',{'object_list':result})
    except:
        return HttpResponse("Not Found")

def tag(request, name):
    try:
        tag = get_object_or_404(Tag, name=name)
        result = tag.content.all()
        return render(request,'search_result.html',{'object_list':result})
    except:
        return HttpResponse("Not Found")



