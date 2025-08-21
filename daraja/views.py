import json
from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def trigger(request):
    cl = MpesaClient() # type: ignore
    phone_number = '0705201338'
    amount = 1
    account_reference = 'test123'
    transaction_desc = 'chapo beans'
    callback_url = 'https://blessed-probably-marmoset.ngrok-free.app/callback'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

@csrf_exempt
def callback(request):
    result = json.loads(request.body)
    print(result)
    
    
    return HttpResponse('Callback received successfully')