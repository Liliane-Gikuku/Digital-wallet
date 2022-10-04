from django.shortcuts import render, redirect



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


def customer_profile(request, id):
    customer=Customer.objects.get(id=id)
    return render(request, "myproject/customer_profile.html", {"customer":customer})


def edit_profile(request,id):
    customer= Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST, instance=Customer)
        
        if form.is_valid():
            form.save()
            
        return redirect("customer_profile", id=customer.id)
    else:
       form=CustomerRegistrationForm(instance=Customer)
       return render(request, "myproject/edit_profile.html", {"form":form})



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


def wallet_profile(request, id):
    wallet=Wallet.objects.get(id=id)
    return render(request, "myproject/wallet_profile.html", {"wallet":wallet})


def edit_wallet(request,id):
    wallet= Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST, instance=Wallet)
        
        if form.is_valid():
            form.save()
            
        return redirect("wallet_profile", id=wallet.id)
    else:
       form=WalletRegistrationForm(instance=Wallet)
       return render(request, "myproject/edit_wallet.html", {"form":form})


def register_account(request):
   if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form=AccountRegistrationForm()
   return render(request,"myproject/register_account.html",{"form":form})

def account_profile(request, id):
    account=Account.objects.get(id=id)
    return render(request, "myproject/account_profile.html", {"account":account})


def edit_account(request,id):
    account= Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST, instance=Account)
        
        if form.is_valid():
            form.save()
            
        return redirect("account_profile", id=account.id)
    else:
       form=AccountRegistrationForm(instance=Account)
       return render(request, "myproject/edit_account.html", {"form":form})

def register_transaction(request):
     if request.method=="POST":
        form=TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
     else:
        form=TransactionRegistrationForm()
     return render(request,"myproject/register_transaction.html",{"form":form})
 
def transaction_profile(request, id):
    transaction=Transaction.objects.get(id=id)
    return render(request, "myproject/transaction_profile.html", {"transaction":transaction})


def edit_transaction(request,id):
    transaction= Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST, instance=Transaction)
        
        if form.is_valid():
            form.save()
            
        return redirect("transaction_profile", id=transaction.id)
    else:
       form=TransactionRegistrationForm(instance=Transaction)
       return render(request, "myproject/edit_transaction.html", {"form":form})

def register_card(request):
     if request.method=="POST":
        form=CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
     else:
        form=CardRegistrationForm()
     return render(request,"myproject/register_card.html",{"form":form})
 
 
def card_profile(request, id):
    card=Card.objects.get(id=id)
    return render(request, "myproject/card_profile.html", {"card":card})


def edit_card(request,id):
    card= Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST, instance=Card)
        
        if form.is_valid():
            form.save()
            
        return redirect("card_profile", id=card.id)
    else:
       form=CardRegistrationForm(instance=Card)
       return render(request, "myproject/edit_card.html", {"form":form})

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


def receipt_profile(request, id):
    receipt=Receipt.objects.get(id=id)
    return render(request, "myproject/receipt_profile.html", {"receipt":receipt})


def edit_receipt(request,id):
    receipt= Receipt.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST, instance=Receipt)
        
        if form.is_valid():
            form.save()
            
        return redirect("receipt_profile", id=receipt.id)
    else:
       form=ReceiptRegistrationForm(instance=Receipt)
       return render(request, "myproject/edit_receipt.html", {"form":form})

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

