from django.db import models



# Create your models here.
class reservation(models.Model):

    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    nom = models.CharField(max_length=50, verbose_name="Nom")
    mot_de_passe = models.CharField(max_length=50, verbose_name="Mot de passe")
    date_naissance = models.DateField(verbose_name = "Date de naissance")
    adresse = models.CharField(max_length=150, verbose_name="Adresse")
    email = models.EmailField(max_length=150, verbose_name="Email", null=True, blank=True)
    telephone = models.CharField(max_length=20, verbose_name="Téléphone", null=True, blank=True)
    type_chambre = models.CharField(max_length=10)
    ville = models.CharField(max_length=100,verbose_name="ville", null=True, blank=True)
    pays = models.CharField(max_length=100,verbose_name="pays", null=True, blank=True)
    
    
    
    
class connexion(models.Model):
    email = models.EmailField(max_length=150, verbose_name="Email", null=True, blank=True)
    mot_de_passe = models.CharField(max_length=50, verbose_name="Mot de passe")
    
    
    
class contact(models.Model):
    nom = models.CharField(max_length=50, verbose_name="Nom")
    email = models.EmailField(max_length=150, verbose_name="Email", null=True, blank=True)
    message = models.CharField(max_length=2000, verbose_name="message")