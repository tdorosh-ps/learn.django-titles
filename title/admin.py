from django.contrib import admin
from .models import Title, IncomingLetter, OutgoingLetter, Counterparty
# Register your models here.
admin.site.register(Title)
admin.site.register(IncomingLetter)
admin.site.register(OutgoingLetter)
admin.site.register(Counterparty)