from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)

    # changing representation of drink,by havving a method on drink object
    def __str__(self):
        return self.name + ' - ' + self.description
