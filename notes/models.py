from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name='date published', default=timezone.now())

    def __str__(self):
        return self.title

