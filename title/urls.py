from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
    path('', views.title_list, name='home'),
  
]