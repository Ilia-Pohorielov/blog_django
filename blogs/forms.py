from django import forms
from .models import Post, Comment, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'status', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about', 'phone']