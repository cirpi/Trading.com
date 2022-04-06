from importlib import import_module

from django.http import HttpResponse
from .models import Balance, Stock
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ConfirmForm, SearchForm
from .apis import request as api_request

# Create your views here.


@login_required
def buy(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        stocks = Stock.objects.all()
        if form.is_valid():
            ticker = form.cleaned_data.get('ticker').upper()
            name = form.cleaned_data.get('name')
            if ticker and name:
                stocks = Stock.objects.filter(
                    ticker__contains=ticker, name__icontains=name)
            elif not ticker:
                stocks = Stock.objects.filter(name__icontains=name)
            elif not name:
                stocks = Stock.objects.filter(ticker__contains=ticker)
    else:
        stocks = Stock.objects.all()
        form = SearchForm()
    return render(request, 'transactions/buy.html', {'stocks': stocks, 'form': form})


@login_required
def sell(request):
    return render(request, 'transactions/sell.html')


@login_required
def confirm(request, ticker):
    if request.method == 'POST':
        print(request.POST)
        form = ConfirmForm(request.POST)
        data = api_request.get_price(ticker, '2020-10-14')
        stock = Stock.objects.get(ticker=ticker)
        if data['status'] != 'NOT_FOUND':
            max = Balance.objects.get(
                user=request.user).total / float(data['high'])
            min = max / 100
        else:
            max = 1
            min = 0.1
        if form.is_valid():
            return HttpResponse('Success')
        pass

    else:
        data = api_request.get_price(ticker, '2020-10-14')
        stock = Stock.objects.get(ticker=ticker)
        if data['status'] != 'NOT_FOUND':
            max = Balance.objects.get(
                user=request.user).total / float(data['high'])
            min = max / 100
        else:
            max = 1
            min = 0.1
        form = ConfirmForm()
    return render(request, 'transactions/confirm.html', {'data': data, 'form': form, 'stock': stock, 'max': round(max, 2), 'min': round(min, 3)},)
