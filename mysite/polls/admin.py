from django.contrib import admin
import os

# Register your models here.
from .models import people
from .models import Customer
from .models import Vehicle
from .models import ACCT_Form

from .fill_form_watermark import makePDF

def populatePDF(modelAdmin, request, queryset):
    people = queryset.values()
    print(people)
    for person in people:
        print(person['person_name'])
        if os.path.exists('overlay_PDF.pdf'):
            print('euruka')
            os.remove('overlay_PDF.pdf')
        makePDF(person)

# class CustomerInline(admin.TabularInline):
#     model = Customer
#     fk_name = "id"

class VehicleInline(admin.TabularInline):
    model = Vehicle
    fk_name = "Customer"

class peopleAdmin(admin.ModelAdmin):
    list_display = ['person_name', 'age']
    ordering = ['person_name']
    actions = [populatePDF]
    # inlines = [VehicleInline, ]
    
# class VehicleAdmin(admin.ModelAdmin):
#     list_display = ['v_make', 'id']
#     ordering = ['v_make']
#     inlines = [CustomerInline, ]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cu_first_name', 'id']
    ordering = ['cu_first_name']
    inlines = [VehicleInline, ]




admin.site.register(people, peopleAdmin)

admin.site.register(Customer, CustomerAdmin)

admin.site.register(Vehicle)

admin.site.register(ACCT_Form)