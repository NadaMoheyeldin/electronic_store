from django.db import models
from category.models import *


class Product(models.Model):
    name = models.CharField(max_length=100)
    insertdate = models.DateTimeField(auto_now_add=True)  # Using DateTimeField
    updatedate = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='products/imgs')
    category = models.ForeignKey(to =Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    @classmethod
    def add(cls,name,image,catid):
        cls.objects.create(
            name=name,
            image=image,
            category=Category.getbyid(id)
        )

    @classmethod
    def getall(cls):
        return cls.objects.filter(status=True)#3shan myzharsh m3aya el soft delete lma a3mel select


    @classmethod
    def hdel(cls,id): #hard delete
        return cls.objects.filter(pk=id).delete()

    @classmethod
    def sdel(cls, id):  # soft delete
        return cls.objects.filter(pk=id).update(status=False)

    @classmethod
    def getbyid(cls,id):
        return cls.objects.get(pk=id, status=True)
