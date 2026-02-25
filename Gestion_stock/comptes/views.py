from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm, ConnexionForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render (request, 'base.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = InscriptionForm()
    return render( request, 'comptes/inscription.html', {'form':form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            utilisateur = form.get_user()
            login(request, utilisateur)
            return redirect('list_produit')
    else :
        form =ConnexionForm()
    return render(request, 'comptes/connexion.html', {'form':form} )


@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

