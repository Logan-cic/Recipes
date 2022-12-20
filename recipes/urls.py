from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # dominioAnterior/sobre/
    path('cotato/', contato),  # dominioAnterior/contato/
]
