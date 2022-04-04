import csv

from django.http import HttpResponse
from .forms import BuyForm
from .models import Stock
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



@login_required
def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            stock = Stock.objects.get(ticker=form.cleaned_data.get('ticker'))
            return HttpResponse(f'<h1 style="text-align: center;">{stock}</h1>')
    else:
        form = BuyForm()
    return render(request, 'transactions/buy.html', {'form':form})

@login_required
def sell(request):
    return render(request, 'transactions/sell.html')

