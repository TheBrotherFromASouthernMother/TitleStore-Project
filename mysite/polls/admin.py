from django.contrib import admin

# Register your models here.
from .models import people

from .fill_form_watermark import makePDF

def birthday(modelAdmin, request, queryset):
    people = queryset.values()
    for person in people:
        print(person['person_name'])
        makePDF(person['person_name'])

class peopleAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'age']
    ordering = ['person_name']
    actions = [birthday]


admin.site.register(people, peopleAdmin)
