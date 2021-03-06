from django.urls import path
from . import views


app_name = 'transactions'

urlpatterns = [
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('<str:ticker>/', views.confirm, name='confirm'),
]
