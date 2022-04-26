from django.db import models
from django.urls import reverse

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f"The dog named {self.name} has an id of {self.id}"

    # once POST request is made, this redirects client to detail page
    #  w/ that dog_id that was just made
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
