from django.db import models

# Create your models here.
class Todos(models.Model):
    task=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task