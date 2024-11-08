from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return render(request, 'main/index.html',{'caption': 'CatDjango'})
    data = {
        'caption': 'CatDjango'
    }
    return render(request, 'main/index.html', data)

def our_cats(request):
    data = {
        'caption': 'CatDjango',
        'cat1': 'Мурзик',
        'cat2': 'Симба'
    }
    return render(request, 'main/cats.html', data)

def affiliate_program(request):
    data = {
        'caption': 'CatDjango'
    }
    return render(request, 'main/affiliate_program.html', data)

def community(request):
    data = {
        'caption': 'CatDjango'
    }
    return render(request, 'main/community.html', data)

def training(request):
    data = {
        'caption': 'CatDjango'
    }
    return render(request, 'main/training.html', data)