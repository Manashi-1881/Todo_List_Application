from django.db import models

# Create your models here.
class Todo(models.Model):
    text=models.CharField(max_length=50)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.text
