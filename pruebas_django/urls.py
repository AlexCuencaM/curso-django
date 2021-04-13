from django.urls import path
from . import views
# app_name="pruebas_django
urlpatterns = [
    path('<int:id>/',views.test, name="test"),
    path('contacts/',views.contacts, name='contacts'),
    path('prueba_extend/', views.prueba_extend, name='prueba_extend'),
    path('', views.index, name="index" ),
]