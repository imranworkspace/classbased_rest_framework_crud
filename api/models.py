from django.db import models

# Create your models here.
class StudentModel(models.Model):
    sname = models.CharField(max_length = 25)
    semail = models.EmailField()
    
    def __str__(self) -> str:
        return self.sname