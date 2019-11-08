from django.db import models

class Bank(models.Model):
    BIC = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    master_account = models.CharField(max_length=200)
    address = models.CharField(max_length=500)


    def __str__(self):
        return self.name
