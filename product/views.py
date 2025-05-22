from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from category.models import Category
from .forms import ProductFormModel
from .forms import ProductForm
from .models import Product
import os
from django.views import View
from django.conf import settings

from django.views.generic import ListView


class Product_list(ListView):
    model = Product
    queryset = Product.getall()
    context_object_name = 'product'
    template_name = 'product/list.html'

##class based
'''class Products_list(View):
    def get(self,request):

        context = {'products':Product.getall()}
        return render(request,'product/list.html',context)

class Product_new(View):
    ##GET
    def get(self,request):
        context = {'form':ProductFormModel()}
        return render(request,'product/newform.html',context)

    ##POST
    def post(self,request):
        form=ProductFormModel(data=request,files=request.FILES)
        if form.is_bound and form.is_valid():
            form.save()
            redirect('product_list')
        else:
            context = {'form': form}




# Create your views here.
def product_list(request):
    context = {'products':Product.getall()}
    return render(request, 'product/list.html',context)#another type of response, go to template loader => translate the html file then return it into string

def product_new(request):
    #print(request.method) #GET
    contex  = {'cats':getall()}
    if request.method == 'POST':
        if (request.POST['pname'] and request.FILES['pimg'] and request.POST['prodcat']):
            Product.add(
                name=request.POST['pname'],
                image=request.FILES['pimg'],
                categoryid=request.POST['prodcat']

            )
            return redirect('product_list')#name='product_list'
        else:
            contex['msg'] = 'invalid data'
    return render(request, 'product/new.html', contex)

def product_update(request, id):
    oldobj = Product.getbyid(id)  # Or use get_object_or_404(Product, id=id)

    if request.method == 'POST':
        # Handle name
        pname = request.POST.get('pname', '').strip()
        if not pname:
            return render(request, 'product/update.html', {
                'oldobject': oldobj,
                'cats': Category.getall(),
                'error': 'Product name is required'
            })
        oldobj.name = pname

        # Handle image
        if 'pimg' in request.FILES:
            if oldobj.image and os.path.isfile(oldobj.image.path):
                os.remove(oldobj.image.path)
            oldobj.image = request.FILES['pimg']

        # Handle category
        cat_id = request.POST.get('prodcat')
        if cat_id:
            oldobj.category = Category.getbyid(cat_id)

        oldobj.save()
        return redirect('product_list')

    return render(request, 'product/update.html', {
        'oldobject': oldobj,
        'cats': Category.getall()
    })


def product_delete(request, id):
    product = Product.getbyid(id)  # Get the specific product instance

    if request.method == 'POST':
        # Option 1: Soft delete (recommended)
        Product.sdel(id)  # Using your soft delete method

        # Option 2: Hard delete
        # product.delete()  # Direct instance method
        # OR
        # Product.hdel(id)  # Using your class method

        return redirect('product_list')

    return render(request, 'product/delete.html', {'product': product})

def product_show_details(request,id):
    product = Product.getbyid(id)
    if product:
        return render(request, 'product/details.html', {'product':product})

def product_newF(request,id):
    if request.method == 'POST':
        form = ProductFormModel(data=request.POST, files=request.FILES,instance=Product)
        if form.is_valid():
            form.save()  # This automatically saves the Product instance
            return redirect('product_list')  # Ensure this URL name exists
    else:
        form = ProductFormModel(instance=Product)

    return render(request, 'product/newform.html', {'form': form})
def product_updatef(request, id):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/update.html', {'form': form})
'''