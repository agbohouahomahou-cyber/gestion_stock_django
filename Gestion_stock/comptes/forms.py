from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta :
        model =Utilisateur
        fields =['username','email','phone', 'password1','password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text= ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text= ""

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

class ConnexionForm(AuthenticationForm):
    username =forms.CharField(label="Nom d'utilisateur")
    password =forms.CharField(label="mot de pass", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })