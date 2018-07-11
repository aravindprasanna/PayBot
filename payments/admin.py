from django.contrib import admin
from payments.models import CardProfile,BillerProfile,Biller,Transaction

# Register your models here.

admin.site.register(CardProfile)
admin.site.register(BillerProfile)
admin.site.register(Biller)
admin.site.register(Transaction)