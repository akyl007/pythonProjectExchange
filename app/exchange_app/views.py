from django.shortcuts import render
import requests

# Create your views here.
def exchange(request):

    response = requests.get(url='https://v6.exchangerate-api.com/v6/93ac3c0d2fef5bb38d62ad7b/latest/USD').json()
    currencies = response.get('conversion_rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies,
        }


    return render(request, 'exchange_app/index.html',context)