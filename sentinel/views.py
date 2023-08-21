from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import RegistrationForm, CreatePostForm
from django.contrib.auth.decorators import login_required
from .models import Blog

# Authenications
def login_user(request):
    return render(request, 'auth/login.html')

def register(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('sentinel:home')
    return render(request, 'auth/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('')

# Home Page
def  home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

# Create a blog post
@login_required(login_url='sentinel:login')
def createpost(request):
    form = CreatePostForm
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid:
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            return redirect('sentinel:home')

            
    return render(request, 'create_post.html', {'form':form})
