from django.urls import path
from .views import card_profile, customer_profile, edit_account, edit_card, edit_receipt, edit_transaction, edit_wallet, list_account, list_card, list_customers, list_notification, list_receipt, list_thirdparty, list_transaction, receipt_profile, register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,list_currency,list_wallet,list_account,list_receipt,edit_profile, transaction_profile, wallet_profile,wallet_profile,edit_wallet,account_profile

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
    path("notifications/",list_notification,name="notification_list"),
    path("receipts/",list_receipt,name="receipt_list"),
    path("customer/<int:id>/", customer_profile, name="customer_profile"),
    path("customer/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("wallet/<int:id>/", wallet_profile, name="wallet_profile"),
    path("wallet/edit/<int:id>/", edit_wallet, name="edit_wallet"),
    path("account/<int:id>/", account_profile, name="account_profile"),
    path("account/edit/<int:id>/", edit_account, name="edit_account"),
    path("card/<int:id>/", card_profile, name="card_profile"),
    path("card/edit/<int:id>/", edit_card, name="edit_card"),
    path("transaction/<int:id>/", transaction_profile, name="transaction_profile"),
    path("transaction/edit/<int:id>/", edit_transaction, name="edit_transaction"),
    path("receipt/<int:id>/", receipt_profile, name="receipt_profile"),
    path("receipt/edit/<int:id>/", edit_receipt, name="edit_receipt"),
   
   
   
   
   
   
   
   
   
   
   

]
