from django.db import models

# Create your models here.
class Tasktodo(models.Model):
    title=models.CharField(max_length=20)
    category=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=20,null=True)
    date=models.DateField(null=True)
    

    def __str__(self):
        return self.title
