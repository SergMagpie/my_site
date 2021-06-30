from icecream import ic
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from .forms import *
from .models import *
from .utils import *
# Create your views here.


class IndexListView(ListView):
    paginate_by = 3
    model = Exercises
    template_name = 'itstep/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Exercises.objects.filter(is_published=True)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': 'Main page',
            'menu': menu(self.request),
            'cat_selected': 0,
        }
        return dict(list(context.items()) + list(insert_def.items()))


class AboutTemplateView(TemplateView):
    template_name = 'itstep/about.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': 'About the site',
            'menu': menu(self.request),
        }
        return dict(list(context.items()) + list(insert_def.items()))


class AddPostCreateView(LoginRequiredMixin, CreateView):
    model = Exercises
    form_class = AddPostForm
    template_name = 'itstep/addpage.html'
    login_url = 'login'

    def get_initial(self):
        self.initial.update({
            'author': self.request.user
        })
        return self.initial

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': 'Add page',
            'menu': menu(self.request),
        }
        return dict(list(context.items()) + list(insert_def.items()))


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'itstep/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': 'Registration',
            'menu': menu(self.request),
        }
        return dict(list(context.items()) + list(insert_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    template_name = 'itstep/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': 'Login',
            'menu': menu(self.request),
        }
        return dict(list(context.items()) + list(insert_def.items()))

    def get_success_url(self) -> str:
        url = self.get_redirect_url()
        if url:
            return url
        else:
            return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class ShowPostDetailView(DetailView):
    model = Exercises
    template_name = 'itstep/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        insert_def = {
            'title': context['post'].title,
            'menu': menu(self.request),
            'cat_selected': None,
        }
        return dict(list(context.items()) + list(insert_def.items()))


class CategoryListView(ListView):
    paginate_by = 3
    model = Exercises
    template_name = 'itstep/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        self.cat = get_object_or_404(Category, slug=self.kwargs['cat_slug'])
        insert_def = {
            'title': self.cat.name,
            'menu': menu(self.request),
            'cat_selected': self.cat.pk,
        }
        return dict(list(context.items()) + list(insert_def.items()))

    def get_queryset(self):
        return Exercises.objects.filter(cat__slug=self.kwargs['cat_slug'])


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found :(</h1>')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "My site"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'sergmagpie@gmail.com',
                          ['sergmagpie@gmail.com', ])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")

    form = ContactForm()
    return render(request, 'itstep/contact.html', {'form': form,
                                                   'menu': menu(request),
                                                   'title': 'Contact'})
