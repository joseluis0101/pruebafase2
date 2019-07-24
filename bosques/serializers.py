from rest_framework import serializers
from .models import Bosque,Arbol
from datetime import datetime

'''
Serialización del modelo de datos Arbol
'''
class ArbolSerialize(serializers.ModelSerializer):
    class Meta:
        model = Arbol
        fields = ['id','name','type','created_at','updated_at','id_forest']

    '''
    Se sobre escribe el metodo update para actualizar la fecha de actualizacion del registro
    '''
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', datetime.now())
        instance.id_forest = validated_data.get('id_forest', instance.id_forest)
        instance.save()
        return instance

'''
Serialización del modelo de datos Bosque
'''
class BosqueSerialize(serializers.ModelSerializer):
    '''
    Se agrega a la serialización un campo calculado
    '''
    trees_count = serializers.SerializerMethodField('count')
    '''
    ##Consulta y conteo de arboles asignados al bosque
    '''
    def count(self, bosque):
        return Arbol.objects.filter(id_forest=bosque).count()

    class Meta:
        model = Bosque
        fields = ['id','name','type','created_at','updated_at','trees_count']
    '''
    Se sobre escribe el metodo update para actualizar la fecha de actualizacion del registro
    '''
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', datetime.now())
        instance.save()
        return instance
