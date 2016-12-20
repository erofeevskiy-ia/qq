from django.shortcuts import render
from  .models import InfoProd

def prod_list(request):
    prods = InfoProd.objects.all().order_by('prod_date')
    return render(request, 'product/prod_list.html', {'prods': prods})

# Create your views here.
