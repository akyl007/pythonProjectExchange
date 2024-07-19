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
        return render(request, 'exchange_app/index.html', context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from_amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get('to_curr')

        converted = round((currencies[to_curr] / currencies[from_curr]) * from_amount,2)
        context = {
            'from_amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'converted': converted,
        }
        return render(request, 'exchange_app/index.html', context)


