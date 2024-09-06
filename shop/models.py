from django.db import models

# Create your models here.

# we can have one prodcut class in a model in can geneate a table which name is Products and it can also have a differnt coloums
# like title,price,etc.


class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
