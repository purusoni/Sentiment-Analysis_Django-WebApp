from django.urls import path
from . import views

urlpatterns = [
    # your url patterns here
    path('', views.index, name='index'),
]
