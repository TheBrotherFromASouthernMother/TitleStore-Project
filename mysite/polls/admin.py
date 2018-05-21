from django.contrib import admin
import os

# Register your models here.
from .models import people
from .models import Customer
from .models import Vehicle

from .fill_form_watermark import makePDF

def populatePDF(modelAdmin, request, queryset):
    people = queryset.values()
    for person in people:
        print(person['person_name'])
        if os.path.exists('overlay_PDF.pdf'):
            print('euruka')
            os.remove('overlay_PDF.pdf')
        makePDF(person)

class peopleAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'age']
    ordering = ['person_name']
    actions = [populatePDF]

admin.site.register(people, peopleAdmin)

admin.site.register(Customer)

admin.site.register(Vehicle)
