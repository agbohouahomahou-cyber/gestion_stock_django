from django import forms
from .models import *

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produits
        fields = ['nom', 'categories', 'quantite', 'prix']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

class StockForm(forms.ModelForm):
    class Meta :
        model = Stock
        fields =['produits','movement_type','quantite']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })