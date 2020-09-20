from django.shortcuts import render
from .models import SliderData
from .models import Products
from django.core.exceptions import MultipleObjectsReturned
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home_view(request):
    slider_data = SliderData.objects.all()
    products = Products.objects.all()
    gates = Products.objects.filter(prod_cat='gates_and_doors')
    grills = Products.objects.filter(prod_cat='grills')
    tin_sheds = Products.objects.filter(prod_cat='tin_sheds')
    farming_tools = Products.objects.filter(prod_cat='farming_tools')
    air_coolers = Products.objects.filter(prod_cat='air_coolers')
    gauri_makhars = Products.objects.filter(prod_cat='gauri_makhars')
    stairs = Products.objects.filter(prod_cat='stairs')
    shutters = Products.objects.filter(prod_cat='shutters')
    others = Products.objects.filter(prod_cat='others')

    # context = {'data':slider_data,'products':products,'gates':gates,'grills':grills,'tin_sheds':tin_sheds,'farming_tools':farming_tools,'air_coolers':air_coolers,'gauri_makhars':gauri_makhars,'stairs':stairs,'shutters':shutters,'others':others}
    return render(request,'home_app/home.html',{'data':slider_data,'products':products,'gates':gates,'grills':grills,'tin_sheds':tin_sheds,'farming_tools':farming_tools,'air_coolers':air_coolers,'gauri_makhars':gauri_makhars,'stairs':stairs,'shutters':shutters,'others':others})

def search_view(request):
    if request.method == 'POST':
        search_input = request.POST.get('search_input')
        searched_products = Products.objects.filter(prod_head__icontains=search_input)
        if len(searched_products) == 0:
            messages.warning(request,'Sorry, We dont found the product you entered.')
            return redirect('/')
    return render(request,'home_app/search.html', {'searched_products':searched_products})

def prod_details_view(request,id):
    product = Products.objects.get(id=id)
    return render(request,'home_app/prod_details.html',{'product':product})
