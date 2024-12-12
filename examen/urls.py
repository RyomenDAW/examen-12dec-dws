from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    path('', views.index,name="urls_index"),  
    path('', views.index, name='index.html'),  # Página de inicio
    path('promociones/crear_promocion.html', views.crear_promocion, name='crear_promocion'),
    path('promociones/editar_promocion.html/<int:nombre>/', views.editar_promocion, name='editar_promocion'),
    path('promociones/eliminar_promocion/<int:nombre>/', views.eliminar_promocion, name='eliminar_promocion'),    

]       

