from django.db import models
from profanity.validators import validate_is_profane


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, validators=[validate_is_profane])
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[validate_is_profane])
    author = models.CharField(max_length=50, default='none', validators=[validate_is_profane])