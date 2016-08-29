from django.contrib import admin

# Register your models here.
from .models import Criminal, crime, Victim

admin.site.register(Criminal)
admin.site.register(crime)
admin.site.register(Victim)