from django import forms

from .models import Customer, Vehicle


class MyForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

# this doesnt work yet
    def __init__(self, *args, **kwargs):
        self.customerRecord = kwargs.pop('cu_id')
        super(MyForm, self).__init__(*args, **kwargs)