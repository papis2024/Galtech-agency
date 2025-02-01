from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import reservationRegistration, connexionclient, contacterNous
from .models import reservation, connexion, contact
from django.contrib import messages



# Create your views here.
def accueil(request):
    return render(request,'agence/accueil.html')


def home(request):
    return render(request,'agence/home.html')

def login(request):
    if request.method == 'POST':
        fm = connexionclient(request.POST)
        if fm.is_valid():
            email=fm.cleaned_data['email']
            mot_de_passe=fm.cleaned_data['mot_de_passe']
            reg=connexion(mot_de_passe = mot_de_passe, email = email )
            reg.save()
            fm = connexionclient()
            if reg is not None:
                return redirect("reserver")
            else:
                messages.error(request, "L'adresse mail ou le mot de passe entré est incorrect")
    else:
        fm = connexionclient()
    return render(request,'agence/login.html' ,{'form':fm})

def register(request):
    if request.method == 'POST':
        fm = reservationRegistration(request.POST)
        if fm.is_valid():
            pr=fm.cleaned_data['prenom']
            name=fm.cleaned_data['nom']
            mot_de_passe=fm.cleaned_data['mot_de_passe']
            dn=fm.cleaned_data['date_naissance']
            addres=fm.cleaned_data['adresse']
            email=fm.cleaned_data['email']
            tel=fm.cleaned_data['telephone']
            tc=fm.cleaned_data['type_chambre']
            ville=fm.cleaned_data['ville']
            pays=fm.cleaned_data['pays']
            reg=reservation(prenom = pr, nom = name, mot_de_passe = mot_de_passe, date_naissance = dn, adresse = addres, email = email, telephone = tel, type_chambre = tc, ville = ville, pays=pays  )
            reg.save()
            fm = reservationRegistration()
            
    else:
        fm = reservationRegistration()
    return render(request,'agence/register.html',{'form':fm})


def contacter(request):
    cl = []
    if request.method == 'POST':
        fm = contacterNous(request.POST)
        if fm.is_valid():
            nom=fm.cleaned_data['nom']
            email=fm.cleaned_data['email']
            message=fm.cleaned_data['message']
            reg=contact(nom = nom, email = email, message=message)
            reg.save()
            fm = contacterNous()
            
    else:
        fm = contacterNous()
        cl = contact.objects.all()
    return render(request,'agence/contact.html',{'form':fm, 'cl':cl})


def apropos(request):
    return render(request,'agence/apropos.html')

def gallerie(request):
    return render(request,'agence/gallerie.html')


#Cette fonction permet de réserver et d'afficher un client dans un hotel 
def reserver(request):
    if request.method == 'POST':
        fm = reservationRegistration(request.POST)
        if fm.is_valid():
            pr=fm.cleaned_data['prenom']
            name=fm.cleaned_data['nom']
            mot_de_passe=fm.cleaned_data['mot_de_passe']
            dn=fm.cleaned_data['date_naissance']
            addres=fm.cleaned_data['adresse']
            email=fm.cleaned_data['email']
            tel=fm.cleaned_data['telephone']
            tc=fm.cleaned_data['type_chambre']
            ville=fm.cleaned_data['ville']
            pays=fm.cleaned_data['pays']
            reg=reservation(prenom = pr, nom = name, mot_de_passe = mot_de_passe, date_naissance = dn, adresse = addres, email = email, telephone = tel, type_chambre = tc, ville = ville, pays=pays  )
            reg.save()
            fm = reservationRegistration()
            
    else:
        fm = reservationRegistration()
    return render(request,'agence/reserver.html',{'form':fm})


#Cette fonction concerne la gestion des clients qui sont dans la basse de données
def gestion(request):
    if request.method == 'POST':
        fm = reservationRegistration(request.POST)
        if fm.is_valid():
            pr=fm.cleaned_data['prenom']
            name=fm.cleaned_data['nom']
            mot_de_passe=fm.cleaned_data['mot_de_passe']
            dn=fm.cleaned_data['date_naissance']
            addres=fm.cleaned_data['adresse']
            email=fm.cleaned_data['email']
            tel=fm.cleaned_data['telephone']
            tc=fm.cleaned_data['type_chambre']
            ville=fm.cleaned_data['ville']
            pays=fm.cleaned_data['pays']
            reg=reservation(prenom = pr, nom = name, mot_de_passe = mot_de_passe, date_naissance = dn, adresse = addres, email = email, telephone = tel, type_chambre = tc, ville = ville, pays=pays  )
            reg.save()
            fm = reservationRegistration()
            
    else:
        fm = reservationRegistration()
        client = reservation.objects.all()
    return render(request,'agence/gestion_client.html',{'form':fm, 'cli':client})

        


#Cette fonction permet de modifier les informations dans la base de donnees
def modifier_donner(request, id):
    if request.method == 'POST':
            client = reservation.objects.get(pk=id)
            fm = reservationRegistration(request.POST, instance=client)
            if fm.is_valid():
                fm.save()
    else:
        client = reservation.objects.get(pk=id)
        fm = reservationRegistration(instance=client)    
        
    return render(request, 'agence/modifier.html',{'form':fm})








#Cette fonction permet de supprimer les informations dans la base de donnees
def supprimer_donner(request, id):
    if request.method == 'POST':
        client = reservation.objects.get(pk=id) 
        client.delete()
        return HttpResponseRedirect('/')







    

 


