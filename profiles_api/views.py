from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile
from . import serializers
from .models import UserProfile
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



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Uses action  (List, create, retrieve, update, partial_update',
            'Automatically maps URLs using Rounters',
            'Provides more functionality with less code'
        ]

        return Response({
                         'message':'Hello',
                         'a_viewset':a_viewset,
                       })

    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'Message':message
            })
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({
            'hhtp_method':'GET'
        })

    def update(self,request,pk=None):
        """ Updating an object"""
        return Response({
            'http_method':'PUT'
        })

    def partial_update(self,request,pk=None):
        """Update partial"""
        return Response({
            'http_method':'PATCH'
        })

    def destroy(self,request,pk=None):
        """Destroy an object """
        return Response({
            'http_method':'Delete'
        })  

class ProfileViewSet(viewsets.ModelViewSet):    
    """Handle Creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication)
    permission_classes = (UpdateOwnProfile)