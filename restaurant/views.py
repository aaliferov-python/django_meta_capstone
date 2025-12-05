from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, viewsets, generics
from rest_framework.response import Response
from . import models, serializers


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ViewSet):
    permission_classes = permissions.IsAuthenticated

class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class  = serializers.BookingSerializer
    queryset = models.Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated] 
    

@api_view()
@permission_classes([permissions.IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})