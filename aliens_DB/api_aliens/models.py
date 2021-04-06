from django.db import models

class History(models.Model):
    records = models.IntegerField(default=0)
    user = models.CharField(max_length=100)
    matches = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user