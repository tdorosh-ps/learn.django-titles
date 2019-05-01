from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
    path('', views.TitleView.as_view(), name='home'),
  
]