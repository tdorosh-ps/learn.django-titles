from django.urls import path

from . import views

app_name = 'title'
urlpatterns = [
	
	#Titles urls
    path('titles/', views.titles_list, name='titles_list'),
	path('title/add/', views.title_add, name='title_add'),
	path('title/<int:title_id>/', views.title_detail, name='title_detail'),
	path('title/<int:title_id>/edit/', views.title_edit, name='title_edit'),
	path('title/<int:title_id>/delete/', views.title_delete, name='title_delete'),
	
	#Incoming Letters urls
	path('inletters/', views.InlettersListView.as_view(), name='inletters_list'),
	path('inletter/add/', views.inletter_add, name='inletter_add'),
	path('inletter/<int:pk>/edit/', views.InletterEditView.as_view(), name='inletter_edit'),
	path('inletter/<int:pk>/delete/', views.InletterDeleteView.as_view(), name='inletter_delete'),
	
	#Outgoing Letters urls
	path('outletters/', views.OutlettersListView.as_view(), name='outletters_list'),
	path('outletter/add/', views.OutletterAddView.as_view(), name='outletter_add'),
	path('outletter/<int:pk>/edit/', views.OutletterEditView.as_view(), name='outletter_edit'),
	path('outletter/<int:pk>/delete/', views.OutletterDeleteView.as_view(), name='outletter_delete'),
	
	#Counterparty urls
	path('counterparties/', views.CounterpartiesListView.as_view(), name='counterparties_list'),
	path('counterparty/add/', views.CounterpartyAddView.as_view(), name='counterparty_add'),
	path('counterparty/<int:pk>/edit/', views.CounterpartyEditView.as_view(), name='counterparty_edit'),
	path('counterparty/<int:pk>/delete/', views.CounterpartyDeleteView.as_view(), name='counterparty_delete'),
	
]