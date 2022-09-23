from django.db import models
# Create your models here.



class Menu(models.Model):
    TOPPING_CHOICE = [(1,'Pepperoni'),(2,'Mushroom'),(3,'Extra cheese'),(3,'Sausage'),(4,'Onion'),(5,'Black olives'),(6,'Green pepper'),(7,'Fresh garlic'),(8,'Tomato'),(9,'Fresh basil')]

    SIZE_CHOICE = [(1,'Small'),(2,'Medium'),(3,'Large')]

    name = models.CharField(max_length=255)
    price = models.FloatField()
    topping_1 = models.IntegerField(choices=TOPPING_CHOICE,default=1)
    topping_2 = models.IntegerField(choices=TOPPING_CHOICE,default=3)
    topping_3 = models.IntegerField(choices=TOPPING_CHOICE,default=6)
    size = models.IntegerField(choices=SIZE_CHOICE,default=2)
    average_rating = models.FloatField(default=0)
    number_of_ratings = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name