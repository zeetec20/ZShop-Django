from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=13)
    def __str__(self):
        return self.username

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    region = models.CharField(max_length=25)
    province = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    sub_disrict = models.CharField(max_length=25)
    detail = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.id, self.user)
    
    def getOrNull(self, id_user):
        pass
        # address = super().objects.get(user = id_user)
    
    def updateOrCreate(self, id_user):
        pass



