from django.shortcuts import render
from django.views import generic
from .models import Title
# Create your views here.

def title_list(request):
	titles = Title.objects.all()
	titles_dates_unique = titles.dates('entry_datetime', 'year')
	return render(request, 'title/titles_list.html', {'titles': titles, 'titles_dates_unique': titles_dates_unique})
	
def title_add(request):
	pass
	
	
def title_edit(request):
	pass
	
def title_delete(request):
	pass