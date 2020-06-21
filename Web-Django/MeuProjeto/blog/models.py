from django.db import models

# Create your models here.

class Post(models.Model):

    STATUS = (
        ('active', 'Ativo'),
        ('draft' , 'Rascunho')
    )

    title = models.CharField(max_length=200)
    slug  = models.SlugField()
    body  = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    status = models.CharField(max_length=15, choices=STATUS)


class Project(models.Model):
    title       = models.CharField(max_length=200)
    created_at  = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(auto_now=True)
    description = models.TextField() 
    img         = models.ImageField()
    link        = models.TextField()
    author      = models.CharField(max_length=200)
    