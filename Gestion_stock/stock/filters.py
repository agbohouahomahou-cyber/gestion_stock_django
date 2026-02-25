import django_filters
from django import forms
from .models import Produits

class ProduitFiltre(django_filters.FilterSet):

    categories = django_filters.ModelChoiceFilter(
        queryset=Produits.objects.values_list('categories', flat=True).distinct(),
        label="Catégorie",
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

    quantite = django_filters.NumberFilter(
        label="Quantité minimale",
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 10'
        })
    )

    prix = django_filters.NumberFilter(
        label="Prix maximum (FCFA)",
        lookup_expr='lte',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 5000'
        })
    )

    class Meta:
        model = Produits
        fields = ['categories', 'quantite', 'prix']
