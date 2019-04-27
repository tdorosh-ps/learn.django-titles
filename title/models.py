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
	entry_datetime = models.DateTimeFiled(verbose_name='Дата занесення в базу даних', default=timezone.now)
	
	
class IncomingLetter(models.Model):
	pass
	


class OutgoingLetter(model.Models):
	pass
	
	
class Counterparty(model.Models):
	name = models.CharField(verbose_name = 'Назва контрагента', max_length = 256)