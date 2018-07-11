from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .serializers import BillerProfileSerializers,TransactionSerializer
from .models import BillerProfile,Biller,Transaction
from .forms import BillerProfileForm
from .models import CardProfile
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.



class BillerProfileViewSet(viewsets.ModelViewSet):
    queryset = BillerProfile.objects.all()
    serializer_class = BillerProfileSerializers

class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #user_info = User.objects.get(user=request.data["user"])
            #print(user_info)
            #user_card = CardProfile.objects.get(user=user_info.username).card_no
            #user_exp = CardProfile.objects.get(user=user_info.username).expiration

            OUTPUT_JSON = {"clientReferenceInformation": {
                "code": "TC50171_3"
            },
                "processingInformation": {
                    "commerceIndicator": "internet"
                },
                "aggregatorInformation": {
                    "subMerchant": {
                        "cardAcceptorID": "1234567890",
                        "country": "US",
                        "phoneNumber": "650-432-0000",
                        "address1": "900 Metro Center",
                        "postalCode": "94404-2775",
                        "locality": "Foster City",
                        "name": "Visa Inc",
                        "administrativeArea": "CA",
                        "region": "PEN",
                        "email": "test@cybs.com"
                    },
                    "name": "V-Internatio",
                    "aggregatorID": "123456789"
                },
                "orderInformation": {
                    "billTo": {
                        "country": "US",
                        "lastName": "VDP",
                        "address2": "Address 2",
                        "address1": "201 S. Division St.",
                        "postalCode": "48104-2201",
                        "locality": "Ann Arbor",
                        "administrativeArea": "MI",
                        "firstName": "RTS",
                        "phoneNumber": "999999999",
                        "district": "MI",
                        "buildingNumber": "123",
                        "company": "Visa",
                        "email": "test@cybs.com"
                    },
                    "amountDetails": {
                        "totalAmount": "102.21",
                        "currency": "USD"
                    }
                },
                "paymentInformation": {
                    "card": {
                        "expirationYear": "2031",
                        "number": "5555555555554444",
                        "securityCode": "123",
                        "expirationMonth": "12",
                        "type": "002"
                    }
                }
            }

            url = "http://localhost:3000/api/payment"
            r = requests.post(url, OUTPUT_JSON)
            json_object = r.json()
            if r.status_code == 200:
                return Response(json_object, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password=raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})


def home(request):
    return render(request,'home.html')


def biller_profile_list(request):

    data = {}
    print("reached here")
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        serializer = BillerProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def payments(request):

    print("reached here")
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        print("reached here")
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user_info = User.get(user=request.data["user"])
            user_card = CardProfile.objects.get(user=user_info).card_no
            user_exp = CardProfile.objects.get(user=user_info).expiration

            OUTPUT_JSON = {"clientReferenceInformation": {
                "code": "TC50171_3"
            },
                "processingInformation": {
                    "commerceIndicator": "internet"
                },
                "aggregatorInformation": {
                    "subMerchant": {
                        "cardAcceptorID": "1234567890",
                        "country": "US",
                        "phoneNumber": "650-432-0000",
                        "address1": "900 Metro Center",
                        "postalCode": "94404-2775",
                        "locality": "Foster City",
                        "name": "Visa Inc",
                        "administrativeArea": "CA",
                        "region": "PEN",
                        "email": "test@cybs.com"
                    },
                    "name": "V-Internatio",
                    "aggregatorID": "123456789"
                },
                "orderInformation": {
                    "billTo": {
                        "country": "US",
                        "lastName": "VDP",
                        "address2": "Address 2",
                        "address1": "201 S. Division St.",
                        "postalCode": "48104-2201",
                        "locality": "Ann Arbor",
                        "administrativeArea": "MI",
                        "firstName": "RTS",
                        "phoneNumber": "999999999",
                        "district": "MI",
                        "buildingNumber": "123",
                        "company": "Visa",
                        "email": "test@cybs.com"
                    },
                    "amountDetails": {
                        "totalAmount": "102.21",
                        "currency": "USD"
                    }
                },
                "paymentInformation": {
                    "card": {
                        "expirationYear": str(user_exp),
                        "number": str(user_card),
                        "securityCode": "123",
                        "expirationMonth": "12",
                        "type": "002"
                    }
                }
            }

            url = "http://localhost:3000/api/payment"
            r = requests.post(url, OUTPUT_JSON)
            json_object = r.json()
            if r.status_code == 200:
                return Response(json_object, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



