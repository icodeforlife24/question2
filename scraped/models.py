from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateField()
    duration = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

