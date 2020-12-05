from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RegUser(models.Model):
    sex = [
        ('Male', 'male'),
        ('Female', 'female'),
        ('Choose not to say', 'choose not to  say')
    ]
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=20, choices=sex)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.username
    