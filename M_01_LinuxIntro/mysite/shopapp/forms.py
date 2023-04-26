from django import forms

class ProductsForm(forms.Form):
    name = forms.CharField()
    price = forms.DecimalField(min_value=1, max_value=10000000)
    description = forms.CharField(label='Product description', widget= forms.Textarea)