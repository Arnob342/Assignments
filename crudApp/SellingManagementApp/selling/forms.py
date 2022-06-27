from django import forms
from selling.models import Selling

class SellingForm(forms.ModelForm):
    class Meta:
        model = Selling
        fields = "__all__"
