from django.contrib import admin

# Register your models here.
from .models import people

def birthday(modelAdmin, request, queryset):
    print(queryset.filter())

class peopleAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'age']
    ordering = ['person_name']
    actions = [birthday]


admin.site.register(people, peopleAdmin)
