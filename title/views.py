from django.shortcuts import render
from .models import Title
# Create your views here.

def titles_list(request):
	titles = Title.objects.all()
	return render(request, 'title/titles_list.html', {'titles': titles})
	
	
def title_add(request):
	pass
	
	
def title_edit(request):
	pass
	
def title_delete(request):
	pass