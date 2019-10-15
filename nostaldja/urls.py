from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('decade/', views.DecadeList.as_view(), name='decade_list'),
    path('decade/<int:pk>', views.DecadeDetail.as_view(), name='decade_detail'),
    path('fad/', views.FadList.as_view(), name="fad_list"),
    path('fad/<int:pk>', views.FadDetail.as_view(), name="fad_detail")
]