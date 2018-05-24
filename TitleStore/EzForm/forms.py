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






class RequestFormKwargsMixin(object):
    """
    CBV mixin which puts the request into the form kwargs.
    Note: Using this mixin requires you to pop the `request` kwarg
    out of the dict in the super of your form's `__init__`.
    """
    def get_form_kwargs(self):
        kwargs = super(RequestFormKwargsMixin, self).get_form_kwargs()
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"request": self.request})
        return kwargs



class RequestKwargModelFormMixin(object):
    """
    Generic model form mixin for popping request out of the kwargs and
    attaching it to the instance.

    This mixin must precede forms.ModelForm/forms.Form. The form is not
    expecting these kwargs to be passed in, so they must be popped off before
    anything else is done.
    """
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)  # Pop the request off the passed in kwargs.
        super(RequestKwargModelFormMixin, self).__init__(*args, **kwargs)