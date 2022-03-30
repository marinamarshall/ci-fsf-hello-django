from django.db import models

# Create your models here.


class Item(models.Model):
    """ item """
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """ string """
        return self.name
