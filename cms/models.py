from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cms_admin.url_generator import generate_url


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    url = models.CharField(max_length=500, unique=True)
    thumbnail_path = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    content = models.TextField()
    publish_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=250)
    url = models.CharField(max_length=500, unique=True)
    thumbnail_path = models.CharField(max_length=500)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.url


class MenuItem(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    icon_path = models.CharField(max_length=500)
    parent = models.IntegerField(default=0)

    @staticmethod
    def get_all_top_level():
        return MenuItem.objects.all().filter(parent=0)

    @staticmethod
    def get_all_for_parent(par):
        return MenuItem.objects.values('id', 'title', 'link').filter(parent=par)


class StaticPage(models.Model):
    title = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    url = models.CharField(max_length=500, unique=True)
    publish_date = models.DateTimeField()
    contents = models.TextField(default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def generate_url(self):
        self.url = generate_url(self.title)
