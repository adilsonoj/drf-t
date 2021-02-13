from rest_framework import serializers
from conta.models import Account, Client, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientAccountSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionClientSerializer(serializers.ModelSerializer):
     client = ClientAccountSerializer(read_only=True)
     class Meta:
        model = Transaction
        fields = '__all__'