from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('section/<slug:slug>/', views.section_detail, name='section_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]