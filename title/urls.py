from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
	
	#Titles urls
    path('', views.title_list, name='home'),
	path('add/', views.title_add, name='title_add'),
	path('<int:title_id>/', views.title_detail, name='title_detail'),
	path('<int:title_id>/edit/', views.title_edit, name='title_edit'),
	path('<int:title_id>/delete/', views.title_delete, name='title_delete'),
]