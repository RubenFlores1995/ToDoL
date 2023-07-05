from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', index_todo, name='index'),
    path('crear', crear_todo, name='crear'),
    path('borrar/<int:pk>', borrar_todo),
    path('detalle/<int:pk>', detalle_todo),
    path('actualizar/<int:pk>', actualizar_todo),
]