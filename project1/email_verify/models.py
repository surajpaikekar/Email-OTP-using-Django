from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    otp = models.CharField(max_length=255, unique=True ,null=True, blank=True)

    def __str__(self):
        return self.email