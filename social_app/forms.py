from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['context', 'image']





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'









