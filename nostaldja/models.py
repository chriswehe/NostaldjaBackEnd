from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.CharField(max_length=64)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    image_url = models.CharField(max_length=500, null=True)
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')