from django.db import models


chain_types = [
    ('Proof of Work', 'Proof of Work'),
    ('Proof of Stake', 'Proof of Stake'),
    ('Other', 'Other')
]


class Currency(models.Model):
    chain_name = models.CharField(max_length=60)
    coin_unit = models.CharField(max_length=60)
    chain_type = models.CharField(max_length=200, choices=chain_types)
    launch_date = models.DateField(auto_now=False, auto_now_add=False, default="2021-03-30")

    Currencies = models.Manager()

    def __str__(self):
        return self.chain_name


class CoinStatus(models.Model):
    # This field (one to one foreign key) is an object of the reference model class
    currency = models.OneToOneField(Currency, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=20, decimal_places=6)
    as_of_date = models.DateField(auto_now=False, auto_now_add=False)
    supply = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    transactions_per_sec = models.DecimalField(max_digits=20, decimal_places=2)

    CoinStatuses = models.Manager()

    def __str__(self):
        return self.currency.chain_name
