from django.db import models

# Create your models here.
class place(models.Model):
   name=models.CharField(max_length=100)
   img=models.ImageField(upload_to='pictures')
   desc=models.TextField()
   price=models.IntegerField()
   offer=models.BooleanField(default=False)
class blog(models.Model):
   img=models.ImageField(upload_to='pictures')
   day = models.IntegerField()
   month = models.CharField(max_length=100)
   desc = models.TextField()

