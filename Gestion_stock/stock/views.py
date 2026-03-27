from django.shortcuts import render, redirect, get_object_or_404
from . forms import ProduitForm, StockForm
from .models import Produits, Stock
from django.db.models import Q
from django.db.models import Sum
from django.core.paginator import Paginator
from .filters import ProduitFiltre
from datetime import datetime
from django.contrib.auth.decorators import login_required

# CRUD/ Gestion des produits 
@login_required
def ajout_produits(request):
    if request.method =='POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_produit')
    else :
        form =ProduitForm()
    return render(request, 'stock/ajout_produits.html', {'form':form} )

@login_required
def modifier_produts(request, id_produit):
    produits=get_object_or_404(Produits,id=id_produit)
    if request.method == 'POST':
        form =ProduitForm(request.POST, instance=produits)
        if form.is_valid():
            form.save()
            return redirect('list_produit')
    else :
        form=ProduitForm(instance=produits)        
    return render(request, 'stock/modifier_produts.html', {'form': form} )
@login_required
def supprimer_produits(request,id_produit):
    produits=get_object_or_404(Produits,id =id_produit)
    if request.method =='POST':
        produits.delete()
        return redirect('list_produit')
    return render(request, 'stock/supprimer_produits.html',{'produits':produits} )

def list_produit(request):
     query = request.GET.get('q')
     produits = Produits.objects.all()
     if query :
         query=query.strip()
         produits = Produits.objects.filter(
             Q(nom__icontains=query) # Recherche par nom
         )
     produitsfilters=ProduitFiltre(request.GET , queryset=produits) #Filtre par categories, quantite et par prix 
     produits=produitsfilters.qs

     pagination = Paginator(produits,5)
     page_number=request.GET.get('page')
     produits =pagination.get_page(page_number)
    
     return render(request, 'stock/list_produit.html', {'produits':produits,
                                                        'produitsfilters':produitsfilters
                                                        } )

def detail_produits(request,id_produit):
    produits=get_object_or_404(Produits,id=id_produit)
    return render(request,'stock/detail_produits.html', {'produits':produits} )


# Gestion des movement du stock

@login_required
def mouvement_stock(request):
    if request.method =='POST':
        form =StockForm(request.POST)
        if form.is_valid():
            mouvement = form.save()
            produits=mouvement.produits
            
            if mouvement.movement_type == 'IN':
                produits.quantite +=mouvement.quantite
            else :
                if mouvement.quantite > produits.quantite :
                    form.add_error('quantite', "la quantitedemandée dépasse le stock disponible")
                    return render(request, 'stock/mouvement_stock.html',{'form':form} )
                produits.quantite -= mouvement.quantite
            
            produits.save()
            return redirect('mouvement_list')
        
    else :
        form= StockForm()     
    return render(request, 'stock/mouvement_stock.html',{'form':form } )

def mouvement_list(request):
    historiques=Stock.objects.order_by('-date')
    return render(request, 'stock/mouvement_list.html',{'historiques':historiques} )


def dashboard(request):

    total_produits = Produits.objects.count()

    stock_total = Produits.objects.aggregate(
        total=Sum('quantite')
    )['total'] or 0

    total_entrees = Stock.objects.filter(
        movement_type='IN'
    ).aggregate(total=Sum('quantite'))['total'] or 0

    total_sorties = Stock.objects.filter(
        movement_type='OUT'
    ).aggregate(total=Sum('quantite'))['total'] or 0

    derniers_mouvements = Stock.objects.select_related(
        'produits'
    ).order_by('-date')[:5]

    context = {
        'total_produits': total_produits,
        'stock_total': stock_total,
        'total_entrees': total_entrees,
        'total_sorties': total_sorties,
        'derniers_mouvements': derniers_mouvements,
    }

    return render(request, 'stock/dashboard.html', context)
