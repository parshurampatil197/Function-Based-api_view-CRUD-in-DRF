from django.db import models

class Items(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True, editable=True)
    subcategory = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, unique=True, editable=True)
    amount = models.PositiveIntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name

