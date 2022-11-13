from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import *
# CustomerViewSet, LoanViewSet, TransactionViewSet,WalletViewSet,AccountViewSet,CardViewSet,ReceiptViewSet



router=routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register(r"wallets",WalletViewSet)
router.register(r"accounts",AccountViewSet)
router.register(r"cards",CardViewSet)
router.register(r"transactions",TransactionViewSet)
router.register(r"loans",LoanViewSet)
router.register(r"receipts",ReceiptViewSet)
router.register(r"notifications",ReceiptViewSet)


urlpatterns = [
      path("",include(router.urls)),
      path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    #   path("deposit/<int:id>",AccountDepositView.as_view(),name='deposit-view'),
      path("transfer/",AccountTransferView.as_view(), name="transfer-view"),
      path("withdrawal/",AccountWithdrawalView.as_view(),name="withrawal-view"),
      path("loan_request/",AccountLoanRequestView.as_view(),name="loan-view"),
      path("loan_repayment/",AccountLoanRepaymentView.as_view(),name="repay-loan-view"),
      path("buy_airtime/",AccountBuyAirtimeView.as_view(),name="repay-loan-view")
     
  ]


  
