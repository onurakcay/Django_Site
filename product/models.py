from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Category(models.Model):
    STATUS = {
        (1, 'Evet'),
        (0, 'Hayır'),
    }
    parent_id = models.IntegerField()
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = {
        (1, 'Evet'),
        (0, 'Hayır'),
    }
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField(blank=True)
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
