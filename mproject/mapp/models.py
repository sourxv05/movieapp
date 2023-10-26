from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(default="unavilable" ,upload_to="image")
def __str__(self):
    return self.name
