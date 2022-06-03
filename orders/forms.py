from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    full_name = forms.CharField(label="Nom complet", widget=forms.TextInput({"class": "form-control", "placeholder": "Nom complet", }))

    email = forms.EmailField(label="Votre email", widget=forms.EmailInput({"class": "form-control", "placeholder": "Votre email", }))

    address = forms.CharField(label="Votre addresse", widget=forms.TextInput({"class": "form-control", "placeholder": "Adresse de livraison", }))

    phone = forms.CharField(label="Telephone", widget=forms.TextInput({"class": "form-control", "placeholder": "Telephone", }))

    class Meta:
        model = Order
        fields = ("full_name", "email", "address", "phone")
