from django.shortcuts import render
from django.views import generic
from .models import Title
# Create your views here.

class TitleView(generic.ListView):
	template_name = 'title/titles_list.html'
	context_object_name = 'titles'
	
	def get_queryset(self):
		return Title.objects.all()
	
	
def title_add(request):
	pass
	
	
def title_edit(request):
	pass
	
def title_delete(request):
	pass