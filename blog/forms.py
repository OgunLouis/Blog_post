from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

from django import forms
from .models import Profile

class ProfileForm(forms.Form):
    image = forms.ImageField(required=False)
    about = forms.CharField(widget=forms.Textarea)
    age = forms.IntegerField(required=False)

