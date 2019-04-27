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
	ministry_agreement = models.Boolean(default=True)
	incoming_letter = models.ManyToManyField('IncomingLetter', verbose_name='Вхідний супрводжувальний лист', blank=True, null=True)
	outcoming_letter = models.ManyToManyField('OutcomingLetter', verbose_name='Вихідний супроводжувальний лист', blank=True, null=True)
	is_done = models.Boolean(vervose_name = 'Виконано', default=False)
	notes = models.TextField(verbose_name='Примітки', blank=True, null=True)
	entry_datetime = models.DateTimeFiled(verbose_name='Дата і час занесення в базу даних', default=timezone.now)
	
	
class IncomingLetter(models.Model):
	receiving_date = models.DateField(verbose_name='Дата реєстрації листа', default=datetime.date.today)
	receiving_number = models.CharField(verbose_name='Реєстраційний номер', max_length = 50)
	sender = models.ForeignKey('Counterparty', verbose_name='Відправник', on_delete=models.PROTECT)


class OutgoingLetter(model.Models):
	sending_date = models.DateField(verbose_name='Дата реєстрації листа', default=datetime.date.today)
	sending_number= models.CharField(verbose_name='Реєстраційний номер', max_length = 50)
	receiver = models.ManyToManyField('Counterparty', verbose_name='Отримувач', on_delete=models.PROTECT)
	
class Counterparty(model.Models):
	name = models.CharField(verbose_name = 'Назва контрагента', max_length = 256)