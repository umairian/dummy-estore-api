from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/post', views.addCategory),
    path('/categories', views.getCategories)
]