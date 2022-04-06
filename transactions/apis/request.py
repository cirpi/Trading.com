import requests
from decouple import config

def base_url():
    return 'https://api.polygon.io/v1/'

def get_price_url():
    price_url = base_url() + f'open-close/'
    return price_url


def get_price(ticker, date):
    response = requests.get(get_price_url() + f'{ticker}/{date}', params={'adjusted':'true', 'apiKey':config('API_KEY')})
    return response.json()



#get_price('ABC', '2020-10-14')