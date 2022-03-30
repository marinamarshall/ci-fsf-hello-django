from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """ item form """
    class Meta:
        """ meta """
        model = Item
        fields = ['name', 'status']
