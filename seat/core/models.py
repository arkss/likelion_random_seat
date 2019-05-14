from django.db import models

class Babylion(models.Model):
    name = models.CharField(max_length=10)
    part = models.BooleanField()

    def __str__(self):
        return self.name
