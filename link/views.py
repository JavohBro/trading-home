from django.shortcuts import render, redirect

#updated!!!!!!

def home(request):
    return render(request, 'single.html')