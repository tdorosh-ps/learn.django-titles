from django.shortcuts import render
from django.views import generic
from .models import Title
# Create your views here.

def title_list(request):
	titles = Title.objects.all()
	titles_dates_unique = titles.dates('entry_datetime', 'year')
	return render(request, 'title/titles_list.html', {'titles': titles, 'titles_dates_unique': titles_dates_unique})
	
def title_add(request):
	return render(request, 'title/title_add.html', {})
	
def title_edit(request, pk):
	title = Title.objects.get(pk=pk)
	return render(request, 'title/title_edit.html', {'title': title})
	
def title_delete(request, pk):
	title = Title.objects.get(pk=pk)
	return render(request, 'title/title_delete.html', {'title': title})