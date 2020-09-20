from django import forms
from phonenumber_field.formfields import PhoneNumberField

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid phone number (e.g. +9188888888).'
}


class WriteUsForm(forms.Form):
    name = forms.CharField(max_length=50)
    city = forms.CharField(max_length=30)
    mobile = PhoneNumberField(error_messages=my_default_errors)
    prod_buyed = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":20}))