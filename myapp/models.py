from django.db import models


class News(models.Model):
    ndate = models.DateField(null = True)
    title = models.CharField(max_length=250)
