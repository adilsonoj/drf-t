from django.db import models

class Account(models.Model):
    agency = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10)
    bank = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    created_at = models.DateField()

    def __str__(self):
        return self.account_number


class Client(models.Model):
    name = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    


class Transaction(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
   
