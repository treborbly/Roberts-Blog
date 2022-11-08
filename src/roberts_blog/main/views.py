from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.generic import DetailView, CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUser, CreateBlog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.contrib.auth.models import User
# Create your views here.

def signup_page(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home page')
    else:
        form = CreateUser()

        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created successfully!')
                return redirect('login page')
        context= {
            'form': form
        }
        return render(request, 'signup.html', context)

def login_page(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home page')
            else: 
                messages.info(request, 'No account under that credentials.')

        context = {}
        return render(request, 'login.html', context)

@login_required(login_url= 'login page')
def home_page(request, *args, **kwargs):
    blogs = Blog.objects.order_by('-id').all()
    context = {
        'content': blogs,
    }
    return render(request, 'home.html', context)

def user_logout(request, *args, **kwargs):
    logout(request)
    return redirect('login page')

@login_required(login_url= 'login page')
def blog_create_page(request, *args, **kwargs):
    form = CreateBlog()
    if request.method == "POST":
        form = CreateBlog(request.POST)
        if form.is_valid():
            form.cleaned_data['author'] = request.user
            print(form.fields['author'])
            print(form.cleaned_data)
            Blog.objects.create(**form.cleaned_data)
            return redirect('home page')
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'blog-create.html', context)



