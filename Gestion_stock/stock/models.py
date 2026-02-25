from django.db import models
from django.conf import settings

# Create your models here.

class Categories(models.Model):
    nom =models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nom
    
class Produits(models.Model):
    nom =models.CharField(max_length=100)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True,blank=True)
    quantite =models.PositiveIntegerField(default=0)
    prix =models.DecimalField(max_digits=10,decimal_places=2)
    date_creat =models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.nom
    
class Stock(models.Model):
    MOUVEMENT_CHOIX = {
        ('IN','Entre'),
        ('OUT','Sorti'),
    }
    produits = models.ForeignKey(Produits, on_delete=models.CASCADE, null=True)
    movement_type = models.CharField(max_length=3, choices=MOUVEMENT_CHOIX)
    quantite=models.PositiveBigIntegerField()
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movement_type