from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__ (self):
        return self.name


class Product(models.Model):
    ESTADO = (("nuevo", "nuevo"), ("usado", "usado"))

    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    value = models.IntegerField()
    product_type = models.CharField(max_length=10,choices=ESTADO, default='nuevo')
    image = models.ImageField(default='default.jpg', upload_to='product')
    
    def __str__ (self):
        return self.name



class Post(models.Model):

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default= "Te Lo Cambio")
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date= models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,null=True , on_delete=models.SET_NULL)
    image = models.ImageField(default='default.jpg', upload_to='post')
    #product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        #return self.title + ' | ' + str(self.author)
        return self.title 
    
    '''def get_absolute_url(self):
        #return reverse('article-detail', kwargs={"pk": self.pk})
        return reverse('article-detail', args=(str(self.id)))
        #return reverse('home')'''
    
