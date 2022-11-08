from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from profanity.validators import validate_is_profane

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']


class CreateBlog(forms.Form):
    title = forms.CharField( 
        widget=forms.TextInput(attrs={'class': 'blog-title'}),
        validators=[validate_is_profane]
    )
    content = forms.CharField( 
        widget=forms.Textarea(attrs={"class": "blog-content"}),
        validators=[validate_is_profane]
    )
    author = forms.CharField( 
        widget=forms.TextInput(attrs={"class": "blog-author"}), required=False,
        validators=[validate_is_profane]
    )
    #image = forms.ImageField( 

    #)

