from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
    path('', views.titles_list, name='home'),
  
]