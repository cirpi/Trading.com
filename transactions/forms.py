from typing import Any, Mapping, Optional, Union
from django import forms
from .models import Balance, Stock


class BuyConfirmForm(forms.Form):
    quantity = forms.FloatField(required=True)

    def clean_quantity(self):
        quantity = self.cleaned_data.get('qunatity')
        if not quantity:
            raise forms.ValidationError('Quantity must not be empty.')
        return quantity


class SearchForm(forms.Form):
    ticker = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'style':'text-transform: uppercase;', 'class':'my-1'}))
    name = forms.CharField(max_length=100,required=False, widget=forms.TextInput(attrs={'class':'my-1'}))

    def clean(self):
        super().clean()
        ticker = self.cleaned_data.get('ticker')
        name = self.cleaned_data.get('name')
        if not ticker and not name:
            raise forms.ValidationError('Atleast one should not be empty.')


class ConfirmForm(forms.Form):
    quantity = forms.IntegerField(required=True, error_messages={'required':'Quantity must not be empty.'}, widget=forms.NumberInput())