from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    @classmethod
    def getall(cls):
        return cls.objects.all()

    @classmethod
    def getbyid(cls,id):
        return cls.object.get(pk=id)