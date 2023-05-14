from django.db import models

# Create your models here.
class Query(models.Model):
    Email=models.EmailField()
    Name=models.CharField(max_length=20)
    Address=models.TextField()
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Zip=models.IntegerField(default="")
    Comments=models.TextField()
    Date=models.DateField(default="")

    def __str__(self):
        return self.Name
    