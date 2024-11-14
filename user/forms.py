from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registerUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class profileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('image',)


class userUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email',)
