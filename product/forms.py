from django import forms
from category.models import Category
from .models import Product

class ProductFormModel(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category']  # Add other fields as needed