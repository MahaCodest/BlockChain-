from django.db import models

# Create your models here.

class register(models.Model):

   name = models.CharField(max_length=30)
   pass1 = models.TextField()
   pass2 = models.TextField()
   email = models.EmailField()
   mno = models.IntegerField() # chk mobile digit

class login(models.Model):

    name1 = models.CharField(max_length=30)
    pass3 = models.TextField()

class Upload(models.Model):
    img = models.ImageField(upload_to='pics')

