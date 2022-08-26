from django.contrib import admin

# Register your models here.
from .models import Currency, Customer,Wallet,Account,Card,Thirdparty,Notification,Receipt,Loan,Reward,Transaction
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name","address")
    searchFields=("fist_name","last_name","address")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("customer", "balance","status")
    searchFields=("customer", "balance","status")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name", "account_number","account_balance")
    searchFields=("account_name", "account_number","account_balance")
admin.site.register(Account,AccountAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("wallet", "account","issuer")
    searchFields=("wallet", "account","issuer")
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=("account", "issuer","transaction_amount")
    searchFields=("account", "issuer","transaction_amount")
admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("date", "recipient","message")
    searchFields=("date", "recipient","message")
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("date", "receipt_number","amount")
    searchFields=("date", "receipt_number","amount")
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("guaranter", "issuer","wallet")
    searchFields=("guaranter", "issuer","wallet")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("date_of_reward", "recipient","points")
    searchFields=("date_of_reward", "recipient","points")
admin.site.register(Reward,RewardAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("wallet", "transaction_description","transaction_amount")
    searchFields=("wallet", "transaction_description","transaction_amount")
admin.site.register(Transaction,TransactionAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("country", "symbol","amount")
    searchFields=("country", "symbol","amount")
admin.site.register(Currency,CurrencyAdmin)
    
# class WalletAdmin(admin.ModelAdmin):
#     list_display=("first_name", "last_name","address",)
#     searchFields=("fist_name","last_name",)

# admin.site.register(Wallet)
# admin.site.register(Account)
# admin.site.register(Card)
# admin.site.register(Thirdparty)
# admin.site.register(Notification)
# admin.site.register(Receipt)
# admin.site.register(Loan)
# admin.site.register(Reward)
# admin.site.register(Transaction)
# admin.site.register(Currency)