from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.log, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.unlog, name='logout'),

]