from django.core import validators
from django import forms 
from .models import reservation, connexion, contact



class reservationRegistration(forms.ModelForm):
    
    TYPE_CHAMBRE_CHOIX = [
        ('choix', 'Sélectionner'),
        ('simple', 'Simple'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    
   

    type_chambre = forms.ChoiceField(choices=TYPE_CHAMBRE_CHOIX, label='Type de Chambre', initial='choix')
    
    
    class Meta:
        model = reservation
        fields = ['prenom','nom','email','mot_de_passe','date_naissance','adresse','telephone','type_chambre','ville','pays']
        widgets = {
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':"galtechagence20@gmail.com"}),
            'mot_de_passe': forms.PasswordInput(render_value= True, attrs={'class':'form-control'}),
            'date_naissance': forms.DateInput(attrs={'class':'form-control','placeholder': 'jj/mm/aaaa'}, format='%d/%m/%Y'),
            'adresse': forms.TextInput(attrs={'class':'form-control', 'placeholder':"22300 Medina"}),
            'telephone': forms.TextInput(attrs={'class':'form-control'}),
            'ville' : forms.TextInput(attrs={'class':'form-control'}),
            'pays' : forms.TextInput(attrs={'class':'form-control'}),
            
            
        }
        
        
        
class connexionclient(forms.ModelForm):
    class Meta:
        model = connexion
        fields = ['email','mot_de_passe']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':"galtechagence20@gmail.com"}),
            'mot_de_passe': forms.PasswordInput(render_value= True, attrs={'class':'form-control'}),
            
            
            
         }
        
        
        
class contacterNous(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['nom','email','message']
        widgets = {           
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':"galtechagence20@gmail.com"}),
            'message': forms.TextInput(attrs={'class':'form-field'}),
            
            
            
         }
    