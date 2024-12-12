from django.shortcuts import render
from django.db.models import Q,Prefetch
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def mi_error_400(request,exception=None):
    return render(request,"errors/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errors/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errors/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errors/500.html",None,None,500)


def crear_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo procesador en la base de datos
            return redirect('index.html')  # Cambia al nombre de tu URL para la lista
    else:
        form = PromocionForm()

    return render(request, 'promociones/crear_promocion.html', {'form': form})


from django.shortcuts import render, get_object_or_404

def editar_promocion(request, nombre):
    promocion = get_object_or_404(Promocion, nombre=nombre)  # Recupera el procesador por id
    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            return redirect('lista_procesadores')
    else:
        form = PromocionForm(instance=promocion)
    
    return render(request, 'promociones/editar_promocion.html', {'form': form, 'promocion': promocion})



def eliminar_promocion(request, nombre):
    # Usamos get_object_or_404 para manejar objetos inexistentes
    promocion = get_object_or_404(Promocion, nombre=nombre)
    
    if request.method == 'POST':
        try:
            promocion.delete()  # Eliminar el procesador de la base de datos
            return redirect('index.html')  # Redirigir a la lista de procesadores
        except Exception as e:
            # Manejar cualquier error de eliminación (aunque no es común)
            print(f"Error al eliminar el procesador: {e}")
            return render(request, 'eliminar_promocion.html', {'promocion': promocion, 'error': 'Hubo un error al eliminar la promocion.'})
    
    # Si el método es GET, mostramos la página de confirmación
    return render(request, 'promociones/eliminar_promocion.html', {'promocion': promocion})