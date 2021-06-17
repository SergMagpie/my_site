from django.db import models
from django.urls import reverse

# Create your models here.


class Exercises(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    content = models.TextField(blank=True, verbose_name='content')
    photo = models.ImageField(upload_to="photos/", verbose_name='photo')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'My exercises'
        verbose_name_plural = 'My exercises'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
