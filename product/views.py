from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from category.models import Category
from .forms import ProductFormModel
from .forms import ProductForm
from .models import Product
import os
from django.views import View

#class based
class Products_list(View):
    def get(self,request):

        context = {'products':Product.getall()}
        return render(request,'product/list.html')

class Product_new(View):
    #GET
    def get(self,request):
        context = {'form':ProductFormModel()}
        return render(request,'product/newform.html',context)

    #POST
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
    context = {'oldobject':Product.getbyid(id),
               'cats':Category.getall()}
    if request.method=='POST':
        #validation
        oldobj=Product.getbyid(id)
        if os.path.exists('/media/'+oldobj.image.path):
            os.remove('/media/'+oldobj.image.path)

        oldobj.name = request.POST['pname']
        oldobj.image = request.FILES['pimg']
        oldobj.category = Category.getbyid(request.POST['prodcat'])
        oldobj.save()
        return redirect('product_list')#route name
    return render(request, 'product/update.html', context)

def product_delete(request,id):
    return render(request, 'product/update.html')

def product_show_details(request,id):
    product = Product.getbyid(id)
    if product:
        return render(request, 'product/details.html', {'product':product})

def product_newF(request):
    if request.method == 'POST':
        form = ProductFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This automatically saves the Product instance
            return redirect('product_list')  # Ensure this URL name exists
    else:
        form = ProductFormModel()

    return render(request, 'product/newform.html', {'form': form})
def product_updatef(request, id):

    if request.method=='POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=Product)
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=Product)
    return render(request, 'product/update.html', {'form': form})
    oldobj = Product.getbyid(id)
    form = ProductForm(initial={
        'name': oldobj.name,
        'image': oldobj.image,
        'category': oldobj.category.id

    })
    context = {'form': form}
