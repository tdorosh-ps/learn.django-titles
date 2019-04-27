import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Title(models.Model):
	TITLE_TYPES = (
		('OB', "Титул об'єкта будівництва"),
		('PVR', 'Титул на проектно-вишукуальні роботи'),
	)
	title = models.CharField(verbose_name='Назва титулу', max_length=256)
	type = models.CharField(verbose_name='Тип титулу', max_length=3, choices=TITLE_TYPES)
	client = models.ForeignKey('Counterparty', verbose_name='Замовник', on_delete=models.PROTECT)
	ministry_agreement = models.BooleanField(default=True)
	incoming_letter = models.ManyToManyField('IncomingLetter', verbose_name='Вхідний супрводжувальний лист', blank=True)
	outgoing_letter = models.ManyToManyField('OutgoingLetter', verbose_name='Вихідний супроводжувальний лист', blank=True)
	is_done = models.BooleanField(verbose_name = 'Виконано', default=False)
	notes = models.TextField(verbose_name='Примітки', blank=True, null=True)
	entry_datetime = models.DateTimeField(verbose_name='Дата і час занесення в базу даних', default=timezone.now)
	
	class Meta(object):
		ordering = ['entry_datetime', 'is_done']
		verbose_name = 'Титул'
		verbose_name_plural = 'Титули'
	
	def __str__(self):
		return 'Титул {} Замовник {}'.format(self.title, self.client)
	
class IncomingLetter(models.Model):
	receiving_date = models.DateField(verbose_name='Дата реєстрації листа', default=datetime.date.today)
	receiving_number = models.CharField(verbose_name='Реєстраційний номер', max_length = 50)
	sender = models.ForeignKey('Counterparty', verbose_name='Відправник', on_delete=models.PROTECT)
	
	class Meta(object):
		ordering = ['receiving_date']
		verbose_name = 'Вхідний лист'
		verbose_name_plural = 'Вхідні листи'
	
	def __str__(self):
		return 'Від {} від {} № {}'.format(self.sender, self.receiving_date, self.receiving_number)

class OutgoingLetter(models.Model):
	sending_date = models.DateField(verbose_name='Дата реєстрації листа', default=datetime.date.today)
	sending_number= models.CharField(verbose_name='Реєстраційний номер', max_length = 50)
	receiver = models.ManyToManyField('Counterparty', verbose_name='Отримувач')
	
	class Meta(object):
		ordering = ['sending_date']
		verbose_name = 'Вихідний лист'
		verbose_name_plural = 'Вихідні листи'
	
	def __str__(self):
		return 'На {} від {} № {}'.format(self.receiver, self.sending_date, self.sending_number)
	
	
class Counterparty(models.Model):
	name = models.CharField(verbose_name = 'Назва контрагента', max_length = 256)
	
	class Meta(object):
		verbose_name = 'Контрагент'
		verbose_name_plural = 'Контрагенти'
	
	def __str__(self):
		return self.name