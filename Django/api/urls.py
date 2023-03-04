from django.urls import path
from .views import getPlayer, setHighScore, addPlayer

urlpatterns = [
    path('<str:name>', getPlayer),
    path('<str:name>/update', setHighScore),
    path('addPlayer/', addPlayer),
]
