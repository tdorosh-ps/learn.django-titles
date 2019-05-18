from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Title, IncomingLetter, OutgoingLetter, Counterparty
# Create your views here.

#Function for generate unique elements, not view (usefull for generate select option)
def get_unique_list_elements(elements):
	unique_elements = []
	for el in elements:
		if el not in unique_elements:
			unique_elements.append(el)
	return unique_elements
	
def title_detail(request, title_id):
	title = Title.objects.get(pk=title_id)
	return render(request, 'title/title_detail.html', {'title': title})

def titles_list(request):
	titles = Title.objects.all()
	clients = set([client['client_id__name'] for client in titles.values("client_id__name")])
	years = titles.dates('entry_datetime', 'year')
	months = titles.dates('entry_datetime', 'month')
	#Add search logic
	if request.GET.get('search_button') is not None:
		search_request = request.GET.get('search', '').strip()
		titles = titles.filter(title__contains=search_request)
		
	if request.GET.get('filtration_button') is not None:
		data = {}
		if request.GET.get('year'):
			data['entry_datetime__year'] = request.GET.get('year')
			
		if request.GET.get('month'):
			data['entry_datetime__month'] = request.GET.get('month')
		
		if request.GET.get('type'):
			data['type'] = request.GET.get('type')
			
		if request.GET.get('client'):
			data['client__name'] = request.GET.get('client')	
			
		if request.GET.get('agreement') == 'on':
			data['ministry_agreement'] = True
		else:
			data['ministry_agreement'] = False
			
		if request.GET.get('done') == 'on':
			data['is_done'] = True
		else:
			data['is_done'] = False
		
		titles = titles.filter(**data)
		
	
	return render(request, 'title/titles_list.html', {'titles': titles, 'years': years, 'months': months, 'clients': clients})
	
def title_add(request):
	titles = Title.objects.all()
	clients = get_unique_list_elements(titles.values("client_id", "client__name"))
	inletters = IncomingLetter.objects.all()
	outletters = OutgoingLetter.objects.all()
	
	if request.method == 'POST':
		
		if request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect('{}?status_message=Додавання титулу відмінено'.format(reverse('title:titles_list')))
			
		if request.POST.get('submit_button') is not None:
			errors = {}
			data = {'type': request.POST.get('type'), 'notes': request.POST.get('notes')}
			
			title = request.POST.get('title', '').strip()
			if title:
				data['title'] = title
			else:
				errors['title'] = 'Введіть назву титулу'
				
			client = Counterparty.objects.get(pk=request.POST.get('client'))
			data['client'] = client
			
			if request.POST.get('agreement') == 'on':
				data['ministry_agreement'] = True
			else:
				data['ministry_agreement'] = False
			
			if request.POST.get('done') == 'on':
				data['is_done'] = True
			else:
				data['is_done'] = False
				
			date = request.POST.get('date', '')
			if date:
				data['entry_datetime'] = date
			else:
				errors['date'] = 'Введіть дату'
				
			incoming_letters = request.POST.getlist('incoming_letter')
			outgoing_letters = request.POST.getlist('outgoing_letter')
			
			
			if errors:
				return render(request, 'title/title_add.html', {'titles': titles, 'clients': clients, 'inletters': inletters, 'outletters': outletters, 'errors': errors})
			
			else:
				title = Title.objects.create(**data)
				if incoming_letters:
					title.incoming_letter.set(incoming_letters)
				if outgoing_letters:
					title.outgoing_letter.set(outgoing_letters)
				title.save()
				return HttpResponseRedirect('{}?status_message=Титул успішно додано'.format(reverse('title:titles_list')))
			
	return render(request, 'title/title_add.html', {'titles': titles, 'clients': clients, 'inletters': inletters, 'outletters': outletters})
	
	
class TitleEditForm(forms.Form):
	titles = Title.objects.all()
	clients = Counterparty.objects.all()
	inletters = IncomingLetter.objects.all()
	outletters = OutgoingLetter.objects.all()
	TITLE_TYPES = (
		('OB', "Титул об'єкта будівництва"),
		('PVR', 'Титул на проектно-вишукуальні роботи'),
	)
	title = forms.CharField(label='Назва титулу', strip=True, min_length=20, widget=forms.Textarea)
	type = forms.ChoiceField(label='Тип титулу', choices=TITLE_TYPES)
	client = forms.ModelChoiceField(label='Замовник', queryset=clients)
	incoming_letters = forms.ModelMultipleChoiceField(label='Вхідні листи', required=False, queryset=inletters)
	outgoing_letters = forms.ModelMultipleChoiceField(label='Вихідні листи', required=False, queryset=outletters)
	agreement = forms.BooleanField(label='Погодження міністерства', required=False)
	done = forms.BooleanField(label='Виконано', required=False)
	notes = forms.CharField(label='Примітки', strip=True, required=False, widget=forms.Textarea)
	datetime = forms.DateTimeField(label='Дата і час занесення в базу')
	
	
def title_edit(request, title_id):
	title = Title.objects.get(pk=title_id)
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect('{}?status_message=Редагування титулу відмінено'.format(reverse('title:titles_list')))
			
		form = TitleEditForm(request.POST)
		if form.is_valid():
			title.title = form.cleaned_data['title']
			title.type = form.cleaned_data['type']
			title.client = form.cleaned_data['client']
			title.incoming_letter.set(form.cleaned_data['incoming_letters'])
			title.outgoing_letter.set(form.cleaned_data['outgoing_letters'])
			title.ministry_agreement = form.cleaned_data['agreement']
			title.is_done = form.cleaned_data['done']
			title.notes = form.cleaned_data['notes']
			title.entry_datetime = form.cleaned_data['datetime']
			title.save()
			return HttpResponseRedirect('{}?status_message=Титул успішно відредаговано'.format(reverse('title:titles_list')))
	
	else:
		form = TitleEditForm(initial={'title': title.title, 'type': title.type, 
				'client': title.client, 'incomimg_letters': title.incoming_letter,
				'agreement': title.ministry_agreement, 'done': title.is_done,
				'notes': title.notes, 'datetime': title.entry_datetime,
				'incoming_letters': title.incoming_letter.all(), 'outgoing_letters': title.outgoing_letter.all(),
				})
			
	return render(request, 'title/title_edit.html', {'title': title, 'form': form})
	
def title_delete(request, title_id):
	title = Title.objects.get(pk=title_id)
	if request.method == 'POST':
		if request.POST.get('cancel_button') is not None:
			return HttpResponseRedirect('{}?status_message=Видалення титулу скасовано'.format(reverse('title:titles_list')))
			
		if request.POST.get('delete_button') is not None:
			title.delete()
			return HttpResponseRedirect('{}?status_message=Титул успішно видалений.'.format(reverse('title:titles_list')))
			
	return render(request, 'title/title_delete.html', {'title': title})
	
	
class InletterAddForm(forms.ModelForm):
	
	class Meta:
		model = IncomingLetter
		fields = '__all__'
	
def inletter_add(request):
	form = InletterAddForm()
	if request.method == 'POST':
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect('{}?status_message=Додавання вхідного листа відмінено'.format(reverse('title:titles_list')))
			
		form = InletterAddForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('{}?status_message=Вхідний лист успішно доданий.'.format(reverse('title:titles_list')))
	
	return render(request, 'title/inletter_add.html', {'form': form})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	