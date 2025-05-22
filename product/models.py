from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from category.models import Category  # Explicit import is better than *


class Product(models.Model):
    name = models.CharField(max_length=100)
    insertdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/imgs')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @classmethod
    def add(cls, name, image, catid):
        """Creates a new product with the given parameters"""
        return cls.objects.create(
            name=name,
            image=image,
            category=Category.getbyid(catid)  # Fixed: using catid instead of id
        )

    @classmethod
    def getall(cls):
        """Returns all active products (status=True)"""
        return cls.objects.filter(status=True)

    @classmethod
    def get_inactive(cls):
        """Returns inactive products (optional)"""
        return cls.objects.filter(status=False)

    @classmethod
    def hdel(cls, id):  # hard delete
        """Permanently deletes a product"""
        return cls.objects.filter(pk=id).delete()

    @classmethod
    def sdel(cls, id):  # soft delete
        """Marks a product as inactive (soft delete)"""
        return cls.objects.filter(pk=id).update(status=False)

    @classmethod
    def restore(cls, id):  # optional restore method
        """Restores a soft-deleted product"""
        return cls.objects.filter(pk=id).update(status=True)

    @classmethod
    def getbyid(cls, id):
        """Gets a product by ID if it exists and is active"""
        try:
            return cls.objects.get(pk=id, status=True)
        except ObjectDoesNotExist:
            return None  # or raise a custom exception