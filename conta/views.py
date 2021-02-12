from rest_framework import viewsets
from conta.models import Account, Client, Transaction
from .serializer import AccountSerializer, ClientSerializer, TransactionSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """Exibe todos as Contas"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """Exibe todos os Clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """Exibe todos os Clientes"""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
