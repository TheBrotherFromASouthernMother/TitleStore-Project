from django.contrib import admin

# Register your models here.
from .models import people

admin.site.register(people)


from .models import Customer
#from .models import Vehicle
admin.site.register(Customer)
#admin.site.register(Vehicle)