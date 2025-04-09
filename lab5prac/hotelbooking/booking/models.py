from django.db import models

# Create your models here.
class Room(models.Model):
    category=models.CharField(max_length=10, choices=[('1BHK', '1BHK'),('2BHK','2BHK'),]) 
    status=models.CharField(max_length=10, default='Free')
    def __str__(self):
        return f"{self.category} - {self.status}"
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name