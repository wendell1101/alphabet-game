from django.db import models


class GameImage(models.Model):
    name = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='game_images')

    def __str__(self):  
        return self.name
    
    

class Choice(models.Model):
    image = models.ForeignKey(GameImage,on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    correct= models.BooleanField()

    def __str__(self):  
        return self.choice
    

