from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/int:pk/', views.detalle_post, name='detalle_post'),
    path('post/crear/', views.crear_post, name='crear_post'),
    path('autor/crear/', views.crear_autor, name='crear_autor'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('buscar/', views.buscar, name='buscar'),
]