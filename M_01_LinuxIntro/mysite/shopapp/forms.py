from django import forms
from .models import Product
from django.contrib.auth.models import Group
from django.forms import ModelForm

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]

