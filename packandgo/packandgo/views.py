from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'core/home.html')