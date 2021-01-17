from .models import Content
from .models import Comment
from django import forms

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('title','body','pic','district', 'tag')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('text',)