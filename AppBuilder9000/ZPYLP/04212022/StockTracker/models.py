from django.db import models



class StockUser(models.Model):
    StockHolderName = models.CharField(max_length=50)
    StockHolderAddress = models.CharField(max_length=150)
    StockHolderPhone = models.CharField(max_length=25)

    def __str__(self):
        return self.StockHolderName



class StockHolderCompany(models.Model):
    YES = 'Yes'
    NO = 'No'
    FULL_TIME_STATUS = [(YES,'Yes'), (NO, 'No')]

    StockCompanyName = models.CharField(max_length=100)
    CompanyAddress = models.CharField(max_length=100)
    FullTimeStatus = models.CharField(max_length=5, choices=FULL_TIME_STATUS, default=None)

    def __str__(self):
        return self.StockCompanyName


class StockData(models.Model):
    StockCompanyName = models.CharField(max_length=30)
    StockTicker = models.CharField(max_length=20)
    StockPrice = models.FloatField()
    StockAmount = models.FloatField()

    # StockHolderName = models.ForeignKey(StockUser, default=None, on_delete=models.CASCADE)
    # StockUserCompanyName = models.ForeignKey(StockHolderCompany, default=None, on_delete=models.CASCADE)



    def __str__(self):
        return self.StockTicker
