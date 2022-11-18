from django.urls import path
from . import views

urlpatterns = [
    path('', views.retorna_main),
    path('login', views.retorna_login),
    path('cadastro', views.retorna_cadastro),
    path('sobre', views.retorna_sobre),
    path('pesquisar', views.retorna_pesquisar),
]