from django.shortcuts import render
from rest_framework import viewsets
from app.models import Account, Customer, Loan, Notification, Receipt, Transaction,Wallet,Card
from .serializers import CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, TransactionSerializer, WalletSerializer, AccountSerializer,CardSerializer
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

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
    
class AccountDepositView(views.APIView):
  
    def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)
   
class AccountWithdrawalView(views.APIView):
    def post(self,request,pk,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.withdraw(amount)
        return Response (message,status=status)
class AccountTransferView(views.APIView):
    def post(self,request,pk,format=None):
        account_1=Account.objects.get(pk=pk)
        account_id=request.data["destination"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)
        except ObjectDoesNotExist:
            return Response("Account Not Found", status=404)
        message, status = account_1.transfer(account,amount)
        return Response (message,status=status)
class AccountLoanRequestView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.loan_request(amount)
        return Response (message,status=status)
class AccountLoanRepaymentView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.loan_repayment(amount)
        return Response (message,status=status)
class AccountBuyAirtimeView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        airtime_money=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)
        except ObjectDoesNotExist:
            return Response("Account not found",status=404)
        message,status=account.buy_airtime(airtime_money)
        return Response(message,status=status)