from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import Bosque,Arbol
from .serializers import BosqueSerialize,ArbolSerialize
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
import django_filters.rest_framework
from .filters import BosqueFilter, ArbolFilter

'''
La clase BosqueListView maneja los filtros y el metodo POST
'''
class BosqueListView(generics.ListAPIView):
    '''
    Llamada a la clase BosqueFilter para implementar los filtros
    '''
    queryset = Bosque.objects.all()
    serializer_class = BosqueSerialize
    filter_backends = [DjangoFilterBackend]
    filter_class = BosqueFilter

    '''
    Metodo POST para crear un nuevo Bosque
    '''
    def post(self, request):
        bosque = request.data
        serializer = BosqueSerialize(data=bosque)
        if serializer.is_valid(raise_exception=True):
            bosque_save = serializer.save()
        return Response({"success": "Bosque '{}' creado de manera exitoso".format(bosque_save.name)})



'''
La clase BosquesDetail maneja los los metdos GET, PUT y DELETE, estos metodos
requieren el parametro id para poder hacer su función
'''
class BosquesDetail(APIView):
    '''
    Metodo que busca que el registro exista en la base de datos,
    si no regresa 404
    '''
    def get_object(self, pk):
        try:
            return Bosque.objects.get(pk=pk)
        except Bosque.DoesNotExist:
            raise Http404
    '''
    Metodo GET para un solo registro
    '''
    def get(self, request, pk, format=None):
        bosque = self.get_object(pk)
        serializer = BosqueSerialize(bosque)
        return Response(serializer.data)

    '''
    Metodo PUT para modificar un registo regresa 404 si no encuentra el registro
    '''
    def put(self, request, pk, format=None):
        saved_article = get_object_or_404(Bosque.objects.all(), pk=pk)
        '''
        instance = Se envia una instancia del registro que se trabaja en el metdo update
        sobre escrito en el serializer
        data = Se manda el request de la petición
        partial = Se indica que no se requieren todos los atributos del objeto
        '''
        serializer = BosqueSerialize(instance=saved_article, data=request.data,partial=True)
        if serializer.is_valid():
            bosque_saved=serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    Metodo DELETE para eliminar un bosque
    '''
    def delete(self, request, pk, format=None):
        bosque = self.get_object(pk)
        bosque.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''
La clase ArbolDetail maneja los los metdos GET, PUT y DELETE, estos metodos
requieren el parametro id para poder hacer su función
'''
class ArbolDetail(APIView):
    '''
    Metodo que busca que el registro exista en la base de datos,
    si no regresa 404
    '''
    def get_object(self, pk):
        try:
            return Arbol.objects.get(pk=pk)
        except Arbol.DoesNotExist:
            raise Http404

    '''
    Metodo GET para un solo registro
    '''
    def get(self, request, pk, format=None):
        arbol = self.get_object(pk)
        serializer = ArbolSerialize(arbol)
        return Response(serializer.data)

    '''
    Metodo PUT para modificar un registo regresa 404 si no encuentra el registro.
    '''
    def put(self, request, pk, format=None):
        saved_arbol = get_object_or_404(Arbol.objects.all(), pk=pk)
        '''
        instance = Se envia una instancia del registro que se trabaja en el metdo update
        sobre escrito en el serializer
        data = Se manda el request de la petición
        partial = Se indica que no se requieren todos los atributos del objeto
        '''
        serializer = ArbolSerialize(instance=saved_arbol, data=request.data,partial=True)
        if serializer.is_valid():
            arbol_saved=serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    Metodo DELETE para eliminar un arbol
    '''
    def delete(self, request, pk, format=None):
        arbol = self.get_object(pk)
        arbol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
La clase BosqueLArbolDetailistView maneja los filtros y el metodo POST
'''
class ArbolListView(generics.ListAPIView):
    '''
    Llamada a la clase ArbolSerialize para implementar los filtros
    '''
    queryset = Arbol.objects.all()
    serializer_class = ArbolSerialize
    filter_backends = [DjangoFilterBackend]
    filter_class = ArbolFilter

    '''
    Metodo POST para crear un nuevo Bosque
    '''
    def post(self, request):
        arbol = request.data
        serializer = ArbolSerialize(data=arbol)
        if serializer.is_valid(raise_exception=True):
            arbol_save = serializer.save()
        return Response({"success": "Bosque '{}' creado de manera exitoso".format(arbol_save.name)})
