from django.shortcuts import render
from rest_framework import viewsets
from app.models import Account, Customer, Loan, Notification, Receipt, Transaction,Wallet,Card
from .serializers import CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer, AccountSerializer,CardSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    
class WalletViewSet(viewsets.ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer
    
class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    
class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    
class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer
    
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=Receipt.objects.all()
    serializer_class=ReceiptSerializer
    
class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer