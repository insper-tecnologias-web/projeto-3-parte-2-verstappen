from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    driverId = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.driverId


class Team(models.Model):
    teamId = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.teamId