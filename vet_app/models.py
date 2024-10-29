from django.db import models
from django.urls import reverse

class Animal(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)  
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Surgery(models.Model):
    name = models.CharField(max_length=100)  
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Vet(models.Model):
    name = models.CharField(max_length=50)
    years_experience = models.IntegerField()
    animals = models.ManyToManyField(Animal)
    surgery = models.ForeignKey(Surgery,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('v_detail', args=[str(self.id)])


