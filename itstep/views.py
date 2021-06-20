from itstep.forms import AddPostForm
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
# Create your views here.

menu = [
    {'title': "About the site", 'url_name': 'about'},
    {'title': "Add article", 'url_name': 'add_page'},
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
    return render(request, 'itstep/about.html',
                  {'menu': menu,
                   'title': 'About the site'})


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(
        request,
        'itstep/addpage.html',
        {
            'form': form,
            'menu': menu,
            'title': 'Add page',
            'cat_selected': None,
        }
    )


def contact(request):
    return HttpResponse(f'contact')


def login(request):
    return HttpResponse(f'login')


def show_post(request, post_slug):
    post = get_object_or_404(Exercises, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': None,
    }
    return render(request, 'itstep/post.html', context=context)


def show_category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Exercises.objects.filter(cat_id=cat.pk)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': cat.name,
        'cat_selected': cat.pk,
    }
    return render(request, 'itstep/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found :(</h1>')
