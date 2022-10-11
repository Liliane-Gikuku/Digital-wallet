from dataclasses import fields
from rest_framework import serializers
from app.models import Account, Customer, Loan, Notification, Receipt, Transaction,Wallet, Card

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields=("first_name","email","age")
        
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields=("customer","balance","status")
        
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=("account_name", "account_number","account_balance")
        
        
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields=("wallet", "account","issuer")
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields=("wallet", "transaction_description","transaction_amount")
        
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields=("guaranter", "issuer","wallet")
        
class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model= Receipt
        fields=("date", "receipt_number","amount")
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields=("date", "recipient","message")