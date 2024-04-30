from django.db import models

class Client(models.Model):
    username = models.CharField(blank=True, null=True, max_length=150)
    name = models.CharField(max_length=150)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name