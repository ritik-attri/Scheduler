from django.db import models
from datetime import datetime
# Create your models here.

class Tasks(models.Model):
    Date_Time=models.DateTimeField(default=datetime.now(),blank=True)
    URL=models.URLField(max_length=100)