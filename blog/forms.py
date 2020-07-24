from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'text',)

class  uploadfileform(forms.form):
        title = forms.Charfield(mx_length=50)
        file = forms.FileField()
        