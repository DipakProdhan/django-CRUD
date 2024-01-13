from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)

    def __str__(self):
        # return self.name
        return str(self.id)
        
        