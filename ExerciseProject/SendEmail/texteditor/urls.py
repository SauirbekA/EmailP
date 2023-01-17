from django.urls import path,include
from . import views
urlpatterns = [
    path('tedit/', views.index, name='index')
]
