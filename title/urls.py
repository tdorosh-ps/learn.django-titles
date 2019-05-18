from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
	
	#Titles urls
    path('', views.titles_list, name='titles_list'),
	path('<int:title_id>/', views.title_detail, name='title_detail'),
	path('add/', views.title_add, name='title_add'),
	path('<int:title_id>/edit/', views.title_edit, name='title_edit'),
	path('<int:title_id>/delete/', views.title_delete, name='title_delete'),
	
	#Incoming Letters urls
	path('inletter/add/', views.inletter_add, name='inletter_add'),
	
	#Outgoing Letters urls
	path('outletter/add/', views.OutletterAddView.as_view(), name='outletter_add'),
	
	#Counterparty urls
	path('counterparty/add/', views.CounterpartyAddView.as_view(), name='counterparty_add'),
	
]