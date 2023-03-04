from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    high_score = models.IntegerField(default=0, )
