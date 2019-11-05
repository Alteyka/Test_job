from django.db import models

class Bank(models.Model):
    BIC = models.IntegerField()
    name = models.CharField(max_length=200)
    master_account = models.CharField(max_length=200)
    address = models.CharField(max_length=500)


    def __str__(self):
        return self.name
