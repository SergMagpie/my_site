from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
# Create your views here.

menu = [
    {'title': "About the site", 'url_name': 'about'},
    {'title': "Add articl", 'url_name': 'add_page'},
    {'title': "Feedback", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'},
]


def index(request):
    posts = Exercises.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'itstep/index.html', context=context)


def about(request):
    return render(request, 'itstep/about.html', {'menu': menu, 'title': 'About the site'})


def add_page(request):
    return HttpResponse(f'add_page')


def contact(request):
    return HttpResponse(f'contact')


def login(request):
    return HttpResponse(f'login')


def show_post(request, post_id):
    return HttpResponse(f'Archive by {post_id}')

def show_category(request, cat_id):
    posts = Exercises.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': cat_id,
    }
    return render(request, 'itstep/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found :(</h1>')
