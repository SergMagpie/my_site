from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import itertools
from unidecode import unidecode

# Create your models here.


class Exercises(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='content')
    photo = models.ImageField(
        upload_to="photos/", blank=True, verbose_name='photo')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT)
    author = models.ForeignKey(User, blank=True,
                                on_delete=models.CASCADE)

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = unidecode(self.title)
        slug_candidate = slug_original = slugify(value)[:max_length - 3]
        for i in itertools.count(1):
            if not Exercises.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'My exercises'
        verbose_name_plural = 'My exercises'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
