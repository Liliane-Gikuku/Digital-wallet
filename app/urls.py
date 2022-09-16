from django.urls import path
from .views import list_account, list_card, list_customers, list_notification, list_thirdparty, list_transaction, register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,list_currency,list_wallet,list_account
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
    path("reward/", register_reward, name="registration"),
    path("customers/",list_customers,name="customers_list"),
    path("currencies/",list_currency,name="currency_list"),
    path("wallets/",list_wallet,name="wallet_list"),
    path("accounts/",list_account,name="account_list"),
    path("transactions/",list_transaction,name="transaction_list"),
    path("cards/",list_card,name="card_list"),
    path("thirdparties/",list_thirdparty,name="thirdparty_list"),
    path("notifications/",list_notification,name="notification_list")
   
   
   
   
   
   
   
   
   
   
   

]
