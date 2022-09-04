from django.shortcuts import render

from app.models import Notification
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request,"myproject/register_customer.html",{"form":form})

def register_currency(request):
    form=CurrencyRegistrationForm
    return render(request,"myproject/register_currency.html",{"form":form})

def register_wallet(request):
    form=WalletRegistrationForm
    return render(request,"myproject/register_wallet.html",{"form":form})

def register_account(request):
    form=AccountRegistrationForm
    return render(request,"myproject/register_account.html",{"form":form})

def register_transaction(request):
    form=TransactionRegistrationForm
    return render(request,"myproject/register_transaction.html",{"form":form})

def register_card(request):
    form=CardRegistrationForm
    return render(request,"myproject/register_card.html",{"form":form})

def register_thirdparty(request):
    form=ThirdPartyRegistrationForm
    return render(request,"myproject/register_thirdyparty.html",{"form":form})

def register_notification(request):
    form=NotificationRegistrationForm
    return render(request,"myproject/register_notification.html",{"form":form})

def register_receipt(request):
    form=ReceiptRegistrationForm
    return render(request,"myproject/register_receipt.html",{"form":form})

def register_loan(request):
    form=LoanRegistrationForm
    return render(request,"myproject/register_loan.html",{"form":form})

def register_reward(request):
    form=RewardRegistrationForm
    return render(request,"myproject/register_reward.html",{"form":form})


