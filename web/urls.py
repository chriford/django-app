from django.urls import path
from web import views

urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('about/', views.about_view, name='about-page')
    path('posts/', views.PublicPosts, name='basicposts')
]
