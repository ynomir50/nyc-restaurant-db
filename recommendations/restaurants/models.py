from django.db import models

class Borough(models.Model):
    name = models.CharField(max_length = 50)
 
    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    borough = models.ForeignKey(Borough, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    neighborhood = models.ForeignKey(Neighborhood, on_delete = models.PROTECT)
    cuisine = models.CharField(max_length = 50)
    price = models.IntegerField(default = 2)
    rating = models.IntegerField(default = 3)
    comments = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name



