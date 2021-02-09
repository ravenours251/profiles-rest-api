from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.


class HelloApiView(APIView):
    """ Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list APIVIEW features"""
        an_apiview = [
            'Uses HHTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Is mapped mannually URLS'
        ]
        
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'methodd':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial Update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """ Delete an object"""
        return Response({'method':'Delete'})