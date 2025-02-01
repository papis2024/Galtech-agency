from django.contrib import admin
from .models import reservation, connexion, contact

# Register your models here.
@admin.register(reservation)
class reservationAdmin(admin.ModelAdmin):
    list_display = ('id','nom','email', 'mot_de_passe','prenom','telephone','adresse','type_chambre','date_naissance','ville','pays')
    
    
@admin.register(connexion)
class connexionAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'mot_de_passe')
    
    
@admin.register(contact)
class contacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email', 'message')