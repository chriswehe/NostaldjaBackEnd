from rest_framework import generics
from .serializers import DecadeSerializer, FadSerializer
from .models import Decade, Fad

class DecadeList(generics.ListCreateAPIView):
    queryset = Decade.objects.all()
    serializer_class = DecadeSerializer

class DecadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decade.objects.all()
    serializer_class = DecadeSerializer

class FadList(generics.ListCreateAPIView):
    queryset = Fad.objects.all()
    serializer_class = FadSerializer

class FadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fad.objects.all()
    serializer_class = FadSerializer