from django.db import models

# Create your models here.

'''
Modelo de datos para Bosque
'''
class Bosque(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) #Campo Auto capturado
    updated_at = models.DateTimeField(auto_now_add=True)#Campo Auto capturado

'''
Modelo de datos para Arbol
'''
class Arbol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)#Campo Auto capturado
    updated_at = models.DateTimeField(auto_now_add=True)#Campo Auto capturado
    id_forest = models.ForeignKey(Bosque, blank=True, null=True,on_delete=models.CASCADE)#llave foranea de la table bosque

    def create(self, validated_data):
        return Arbol.objects.create(**validated_data)
