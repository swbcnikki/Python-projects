from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Post
from .forms import UserRegisterForm


def home(request):
    return render(request, 'CryptoAnalytics/crypto_analytics_home.html')


def about(request):
    return render(request, 'CryptoAnalytics/about.html', {'title': 'About'})


def register(request):
    form = UserRegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('crypto_home')
        else:
            form = UserRegisterForm()
    return render(request, 'CryptoAnalytics/register.html', {'form': form})


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'CryptoAnalytics/login.html', context={'form': form})


def crypto_display(request):
    all_objects = Post.post.all()

    context = {'all_objects': all_objects}

    return render(request, 'CryptoAnalytics/crypto_display.html', context)


def crypto_details(request, pk):
    details = get_object_or_404(Post, pk=pk)
    context = {'details': details}
    return render(request, 'CryptoAnalytics/crypto_details.html', context)
