import os
from django.db import models
from PIL import Image
import os
from django.conf import settings
# Create your models here.

#if path update is needed inset this in upload_to for ImageField
def image_directory_name(instance,filename):
    image_name = f"{instance.name}_{instance.id}"
    full_path = os.path.join(settings.MEDIA_ROOT,image_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return image_name

class Menu(models.Model):
    TOPPING_CHOICE = [(1,'Pepperoni'),(2,'Mushroom'),(3,'Extra cheese'),(4,'Sausage'),(5,'Onion'),(6,'Black olives'),(7,'Green pepper'),(8,'Fresh garlic'),(9,'Tomato'),(10,'Fresh basil')]

    SIZE_CHOICE = [(1,'Small'),(2,'Medium'),(3,'Large')]

    name = models.CharField(max_length=255)
    price = models.FloatField()
    topping_1 = models.IntegerField(choices=TOPPING_CHOICE,default=1)
    topping_2 = models.IntegerField(choices=TOPPING_CHOICE,default=3)
    topping_3 = models.IntegerField(choices=TOPPING_CHOICE,default=6)
    size = models.IntegerField(choices=SIZE_CHOICE,default=2)
    picture = models.ImageField(upload_to='pizza-images',blank=True,default='pizza-images/no_image.jpg')
    our_rating = models.FloatField(default=0)
    items_in_stock = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        SIZE = 500, 500

        if self.picture:
            image = Image.open(self.picture.path)
            image.thumbnail(SIZE, Image.LANCZOS)
            image.save(self.picture.path)
    
    def __str__(self):
        return self.name