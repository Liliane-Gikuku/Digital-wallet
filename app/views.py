from django.shortcuts import render


from app.models import Account, Card, Currency, Customer, Notification, Receipt, Thirdparty, Wallet, Transaction
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"myproject/register_customer.html",{"form":form})




def register_currency(request):
   if request.method=="POST":
        form=CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form=CustomerRegistrationForm()
   return render(request,"myproject/register_currency.html",{"form":form})



def register_wallet(request):
   if request.method=="POST":
        form=WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form=WalletRegistrationForm()
   return render(request,"myproject/register_wallet.html",{"form":form})


def register_account(request):
   if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form=AccountRegistrationForm()
   return render(request,"myproject/register_account.html",{"form":form})

def register_transaction(request):
     if request.method=="POST":
        form=TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
     else:
        form=TransactionRegistrationForm()
     return render(request,"myproject/register_transaction.html",{"form":form})

def register_card(request):
     if request.method=="POST":
        form=CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
     else:
        form=CardRegistrationForm()
     return render(request,"myproject/register_card.html",{"form":form})

def register_thirdparty(request):
  if request.method=="POST":
        form=ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
          form=ThirdPartyRegistrationForm()
        return render(request,"myproject/register_thirdparty.html",{"form":form})

def register_notification(request):
  if request.method=="SEND":
        form=NotificationRegistrationForm(request.SEND)
        if form.is_valid():
            form.save()
        else:
          form=NotificationRegistrationForm()
        return render(request,"myproject/register_notification.html",{"form":form})

def register_receipt(request):
  if request.method=="SEND":
    form=ReceiptRegistrationForm(request.SEND)
    if form.is_valid():
            form.save()
    else:
          form=ReceiptRegistrationForm()
    return render(request,"myproject/register_receipt.html",{"form":form})

def register_loan(request):
  if request.method=="SEND":
    form=LoanRegistrationForm(request.SEND)
    if form.is_valid():
            form.save()
    else:
          form=LoanRegistrationForm()
    return render(request,"myproject/register_loan.html",{"form":form})

def register_reward(request):
    if request.method=="SEND":
      form=RewardRegistrationForm(request.SEND)
      if form.is_valid():
            form.save()
    else:
          form=RewardRegistrationForm()
    return render(request,"myproject/register_reward.html",{"form":form})

def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"myproject/customers_list.html",{"customers":customers})

def list_currency(request):
    currencies=Currency.objects.all()
    return render(request,"myproject/currency_list.html",{"currencies":currencies})

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"myproject/wallet_list.html",{"wallets":wallets})

def list_account(request):
    accounts=Account.objects.all()
    return render(request,"myproject/account_list.html",{"accounts":accounts})

def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"myproject/transaction_list.html",{"transactions":transactions})

def list_card(request):
    cards=Card.objects.all()
    return render(request,"myproject/card_list.html",{"cards":cards})

def list_thirdparty(request):
    thirdparties=Thirdparty.objects.all()
    return render(request,"myproject/thirdparty_list.html",{"thirdparties":thirdparties})


def list_notification(request):
    notifications=Notification.objects.all()
    return render(request,"myproject/notification_list.html",{"notifications":notifications})


def list_receipt(request):
    receipts=Receipt.objects.all()
    return render(request,"myproject/receipt_list.html",{"receipts":receipts})

