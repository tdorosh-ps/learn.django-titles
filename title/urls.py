from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
	
	#Titles urls
    path('', views.title_list, name='home'),
	path('add/', views.title_add, name='title_add'),
	path('<int:pk>/edit/', views.title_edit, name='title_edit'),
	path('<int:pk>/delete/', views.title_delete, name='title_delete'),
]