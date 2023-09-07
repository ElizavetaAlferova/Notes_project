from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Note(models.Model):
    title = models.CharField(max_length=200)
    composer = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=400, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(verbose_name='date published', default=timezone.now())
    pdf = models.FileField(upload_to='pdf/', blank=True, default=None, null=True, validators=[FileExtensionValidator(['pdf'])])
    image = models.ImageField('Фото', blank=True, upload_to='posts_images')

    class Meta:
        verbose_name ='Ноты'
        verbose_name_plural = 'Ноты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name='date published', default=timezone.now())

    class Meta:
        verbose_name ='Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
