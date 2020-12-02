from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextField()
    image = models.FileField(upload_to='about', blank=True)

    class Meta:
       managed = False
       db_table = 'about'

    def __str__(self):
        return self.title