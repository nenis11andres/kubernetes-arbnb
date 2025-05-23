from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Usuario



def salir(request):
    logout(request)
    return redirect('login')