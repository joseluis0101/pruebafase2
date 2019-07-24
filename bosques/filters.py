import django_filters
from .models import Bosque, Arbol

'''
Filtro de busqueda para Bosque
'''
class BosqueFilter(django_filters.FilterSet):

    class Meta:
        model = Bosque
        fields = ('id','name','type','created_at','updated_at')
'''
Filtro de busqueda para Arbol
'''
class ArbolFilter(django_filters.FilterSet):

    class Meta:
        model = Arbol
        fields = ('id','name','type','created_at','updated_at')
