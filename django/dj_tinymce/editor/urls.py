from django.urls import path
# import local views
from . import views

urlpatterns = [
    path(r'', views.index, name='index-name'), 
]

