from rest_framework import serializers
from payments.models import BillerProfile,Biller,Transaction
from django.contrib.auth.models import User

class BillerProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = BillerProfile
        fields = ('user','biller_name','biller_ref')

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('user','biller_name','biller_ref','amount')