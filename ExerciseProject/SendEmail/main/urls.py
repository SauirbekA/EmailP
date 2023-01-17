from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.main, name='main'),
    path('', views.MyView.as_view(), name='view'),
    path('emailsend/', views.emailsend, name='emailsend')

]