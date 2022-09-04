from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet
urlpatterns =[
    path("register/", register_customer, name="registration"),
    path("currency/", register_currency, name="registration"),
    path("wallet/", register_wallet, name="registration"),
    path("account/", register_account, name="registration"),
    path("transaction/", register_transaction, name="registration"),
    path("card/", register_card, name="registration"),
    path("thirdparty/", register_thirdparty, name="registration"),
    path("notification/", register_notification, name="registration"),
    path("receipt/", register_receipt, name="registration"),
    path("loan/", register_loan, name="registration"),
    path("reward/", register_reward, name="registration")
   
   
   
   
   
   
   
   

]
