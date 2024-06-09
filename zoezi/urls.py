from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('list_view/', views.list_view, name='V_list'),
    path('portfolio/', views.portfolio, name='port'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),

]