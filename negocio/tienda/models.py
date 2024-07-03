from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Default description')

    def __str__(self):
        return self.title

class Chair(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(default='Description not provided')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(default='Description not provided')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Deco(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(default='Description not provided')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
