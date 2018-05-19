from django.contrib import admin

# Register your models here.
from .models import people
from .models import Customer
from .models import Vehicle


admin.site.register(people)

admin.site.register(Customer)

admin.site.register(Vehicle)