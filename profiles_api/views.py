from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """ Test API View"""

    def get(self,request,format=None):
        """Returns a list APIVIEW features"""
        an_apiview = [
            'Uses HHTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Is mapped mannually URLS'
        ]
        
        return Response({'message':'Hello!','an_apiview':an_apiview})