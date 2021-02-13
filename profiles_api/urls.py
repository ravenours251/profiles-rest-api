from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, basename='hello_viewset')
router.register('profiles',views.ProfileViewSet,basename='Profiles')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view(),name='hello_view'),
    path('',include(router.urls)),

]