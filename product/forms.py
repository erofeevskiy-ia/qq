from django import forms
from .models import InfoProd

class ProdForm(forms.ModelForm):

    class Meta:
       model = InfoProd
       fields = ('prod_title', 'prod_count', 'prod_address', 'prod_date', 'prod_status')