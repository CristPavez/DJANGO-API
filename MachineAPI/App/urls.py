
from .views import Lista_PView, ListaView, DataFrame_ModelV
from django.urls import path

urlpatterns = [
  path('lista/',ListaView.as_view(), name='Lista'),
  path('lista/<int:pk>/',Lista_PView.as_view(), name='Numero'),
  path('test/',DataFrame_ModelV.as_view(), name='test')
]