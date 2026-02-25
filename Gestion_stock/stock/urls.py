from django.urls import path
from . import views

urlpatterns = [
    path('ajout_produits/',views.ajout_produits, name='ajout_produits'),
    path('modifier_produts/<int:id_produit>', views.modifier_produts, name='modifier_produts'),
    path('supprimer_produits/<int:id_produit>', views.supprimer_produits, name='supprimer_produits'),
    path('list_produit/', views.list_produit, name='list_produit'),
    path('detail_produits/<int:id_produit>/', views.detail_produits, name='detail_produits'),

    path('mouvement_stock/', views.mouvement_stock, name='mouvement_stock'),
    path('mouvement_list/', views.mouvement_list, name='mouvement_list'),
    path('dashboard/',views.dashboard, name='dashboard')

] 
