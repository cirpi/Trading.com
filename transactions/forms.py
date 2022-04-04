from django import forms
from .models import Stock


class BuyForm(forms.Form):
    ticker = forms.CharField(max_length=20, required=True, widget=forms.TextInput(
        attrs={'style': 'text-transform:uppercase;'}))

    def clean_ticker(self):
        try:
            ticker = self.cleaned_data.get('ticker')
            if not ticker:
                raise forms.ValidationError('Ticker must not be empty.')
            ticker = ticker.upper()
            stock = Stock.objects.get(ticker=ticker)
        except Stock.DoesNotExist:
            raise forms.ValidationError('Not available in NYSE.')
        return ticker


class BuyConfirmForm(forms.Form):
    pass
