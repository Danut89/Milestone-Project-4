from django.db import models

# Create your models here.


class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title
