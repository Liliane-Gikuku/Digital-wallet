from django.contrib import admin

# Register your models here.
from .models import Currency, Customer,Wallet,Account,Card,Thirdparty,Notification,Receipt,Loan,Reward,Transaction
# class CustomerAdmin(admin.ModelAdmin):
#     list_display=("first_name", "last_name","address",)
#     searchFields=("fist_name","last_name",)
    
# class WalletAdmin(admin.ModelAdmin):
#     list_display=("first_name", "last_name","address",)
#     searchFields=("fist_name","last_name",)
admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Transaction)
admin.site.register(Currency)