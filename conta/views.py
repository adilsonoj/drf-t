from rest_framework import viewsets
from conta.models import Account, Client
from .serializer import AccountSerializer, ClientSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """Exibe todos as Contas"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """Exibe todos os Clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
