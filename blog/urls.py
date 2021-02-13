from django.contrib import admin
from django.urls import path, include
from website.views import PostViewSet
from conta.views import AccountViewSet, ClientViewSet, TransactionViewSet, TransactionListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')
router.register('accounts', AccountViewSet, basename='accounts')
router.register('clients', ClientViewSet, basename='clients')
router.register('transactions', TransactionViewSet, basename='transactions')
router.register('transactionlist', TransactionListViewSet, basename='transactionlist')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
