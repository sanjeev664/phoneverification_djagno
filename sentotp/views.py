from django.shortcuts import render
from rest_framework.views import APIView
from twilio.rest import Client
import random
from django.http import JsonResponse
from rest_framework import status

def generateOTP():
    return random.randrange(100000, 999999)


class SendOTP(APIView):
    def post(self, request):
        print("oK request is commig")
        account_sid = "your twilio account ID"
        auth_token = "twilio token"
        print(request.data['number'])
        number = request.data["number"]
        client = Client(account_sid, auth_token)
        otp = generateOTP()
        body =  "Your OTP is " + str(otp)
        message = client.api.account.messages.create(from_="", body=body, to=number)
        if message.sid:
            print("Send Successfully!")
            return JsonResponse({'status': True})
        else:
            print("send Fail")
            return JsonResponse({'status': False})

    
    def get(self, request):
        return JsonResponse({'status': status.HTTP_200_OK})
