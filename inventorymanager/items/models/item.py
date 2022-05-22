from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(default=1)
    

    def __str__(self):
        return self.name