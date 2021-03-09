from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    draft = models.BooleanField(null=False, blank=True, default=True)
    pub_date = models.DateTimeField(verbose_name='Date published', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


