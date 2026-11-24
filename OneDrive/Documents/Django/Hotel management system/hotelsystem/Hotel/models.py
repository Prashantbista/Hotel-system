from django.db import models


# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    table=models.IntegerField()
    email=models.EmailField(max_length=300)
    reservation_time=models.TimeField()
    document=models.FileField(upload_to="documents/", blank=True)

class Worker(models.Model):
      name=models.CharField(max_length=100)
      phone_number = models.CharField(max_length=20)
      email=models.EmailField(max_length=300)
      role = models.CharField(max_length=50, blank=True, null=True)
      salary=models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
      date_hired = models.DateField(auto_now_add=True)

class AIConversation(models.Model):    
 question = models.TextField()    
 answer = models.TextField()    
 created_at = models.DateTimeField(auto_now_add=True)    
 def __str__(self):        
  return self.question[:50]

      