from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet, LoanViewSet, TransactionViewSet,WalletViewSet,AccountViewSet,CardViewSet,ReceiptViewSet


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
  ]


  
