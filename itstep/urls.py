from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('addpage/', AddPostCreateView.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPostDetailView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(),
         name='category'),
]
