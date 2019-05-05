from django.shortcuts import render
from django.views import generic
from .models import Title
# Create your views here.

def title_list(request):
	titles = Title.objects.all()
	unique_clients = set([client['client_id__name'] for client in titles.values("client_id__name")])
	titles_dates_unique = titles.dates('entry_datetime', 'year')
	#Add search logic
	if request.GET.get('search_button') is not None:
		search_request = request.GET.get('search', '').strip()
		titles = titles.filter(title__contains=search_request)
		
	if request.GET.get('filtration_button') is not None:
		data = {}
		if request.GET.get('type'):
			data['type'] = request.GET.get('type')
		else:
			None
			
		if request.GET.get('client'):
			data['client__name'] = request.GET.get('client')
		else:
			None	
			
		if request.GET.get('agreement') == 'on':
			data['ministry_agreement'] = True
		else:
			data['ministry_agreement'] = False
			
		if request.GET.get('done') == 'on':
			data['is_done'] = True
		else:
			data['is_done'] = False
		
		titles = titles.filter(**data)
		
	
	return render(request, 'title/titles_list.html', {'titles': titles, 'titles_dates_unique': titles_dates_unique, 'unique_clients': unique_clients})
	
def title_add(request):
	return render(request, 'title/title_add.html', {})
	
def title_edit(request, pk):
	title = Title.objects.get(pk=pk)
	return render(request, 'title/title_edit.html', {'title': title})
	
def title_delete(request, pk):
	title = Title.objects.get(pk=pk)
	return render(request, 'title/title_delete.html', {'title': title})