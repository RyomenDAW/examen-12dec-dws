from django import forms
from .models import Usuario, Promocion, Producto
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime

class PromocionForm(forms.ModelForm): #MODEL FORM
    class Meta:
        model = Promocion
        fields = 'nombre', 'descripcion_promocion', 'usuarios', 'descuento', 'fecha_inicio_promocion', 'fecha_fin_promocion', 'esta_activa'  # Incluir todos los campos del modelo

        # Configuración opcional para personalizar etiquetas o mensajes de ayuda
        labels = {
            'nombre': 'Nombre de la Promocion',
            'descripcion_promocion': 'Descripcion de promocion',
            'usuarios': 'Usuarios asignados a la promocion',
            'descuento': 'Descuento',
            'fecha_inicio_promocion': 'Fecha de Inicio de la Promocion',
            'fecha_fin_promocion': 'Fecha de Fin de la Promocion',
            'esta_activa': 'La promocion esta activa?',
        }
        help_texts = {
            'descripcion_promocion': 'Redacte la descripcion, recuerda, minimo 100 caracteres',
            'fecha_fin_promocion': 'Fecha de fin de la promocion',
        }
        widgets = {
        'fecha_inicio_promocion': forms.DateInput(attrs={'class': 'form-control'}),
        'fecha_fin_promocion': forms.DateInput(attrs={'class': 'form-control'}),     
}
        
    def clean(self):
 
        #Validamos con el modelo actual
        super().clean()
        
        nombre = self.cleaned_data.get('nombre')
        descripcion_promocion = self.cleaned_data.get('descripcion_promocion')
        usuarios = self.cleaned_data.get('usuarios')
        descuento = self.cleaned_data.get('descuento')
        fecha_inicio_promocion = self.cleaned_data.get('fecha_inicio_promocion')
        fecha_fin_promocion = self.cleaned_data.get('fecha_fin_promocion')
        esta_activa = self.cleaned_data.get('esta_activa')

    #Y aqui empezamos a validar como locos

        #Nombre de la promoción: el nombre tiene que ser único. (0.5)
        
        nombrePromocion = Promocion.objects.get(nombre=nombre)
        if(not nombrePromocion is None):
             self.add_error('nombre','Ya existe un libro con ese nombre')
             
        #Descripción de la promoción: Debe tener al menos 100 caracteres (0.25)

        if len(descripcion_promocion) < 100:
            self.add_error(descripcion_promocion, 'Minimo 100 caracteres')
            
        #Producto de la promoción: El producto debe permitir que tenga promociones (0.75)

        

        #Usuarios a los que se le aplica la promoción: Los usuarios tienen que ser mayor de edad(0.75)
        if usuarios: 
            usuarios_18 = Usuario.objects.filter(edad__gte=18)   #GREATER THAN EQUAL
            for usuario in usuarios:
                if usuario not in usuarios_18:
                    self.add_error('usuarios', 'No tiene 18 aun')        
        #Descuento que se le aplica: Tiene que ser un valor entero entre 0 y 10 (0.25)

        if (descuento) < 0:
            self.add_error(descuento, 'Minimo 0')
        if (descuento) > 10:
            self.add_error(descuento, 'Maximo 10')
            
        #Fecha inicio de la promoción: Esta fecha debe ser inferior a la la fecha fin de la promoción (0.5)
        fecha_inicio_promocion = date.today().strftime("%d-%m-%Y")
        if fecha_inicio_promocion >= fecha_fin_promocion :
             self.add_error('fecha_inicio_promocion','La fecha de inicio de promocion debe ser INFERIOR a la fecha de fin de esta misma')
        
        #Fecha fin de la promoción: Esta fecha no puede inferior a la fecha actual(0.5)
        fechaHoy = date.today().strftime("%d-%m-%Y")
        if fechaHoy < fecha_fin_promocion :
             self.add_error('fecha_fin_promocion','La fecha de fin de promocion NO debe ser menor a Hoy')
        

    
        return self.cleaned_data
    
class BusquedaAvanzadaPromocion(forms.Form):
    nombreBusqueda = forms.CharField(required=False)   
    fecha_inicio_promocion = forms.DateTimeField(required=False)
    fecha_fin_promocion = forms.DateTimeField(required=False)
    descuento = forms.NumberInput()
    usuarios = forms.MultipleChoiceField(required=False)
    es_activa = forms.BooleanField(required=False)
    def clean(self):  
        cleaned_data = super().clean()
    #Texto que busque en nombre y descripción (0,6)
    
    if nombreBusqueda:
    # Aplicamos un filtro que busque en el nombre o la descripción
        nombreBusqueda = nombreBusqueda
        
    #Rango de fechas relacionadas con la fecha fin de la promoción. Buscar por una fecha mayor a la fecha fin y una fecha menor a la fecha fin. (0.6)

    #Búsqueda de promociones con un descuento mayor al indicado (0.6)
        
    #Permitir seleccionar varios usuarios (0.6)

    #Buscar por promociones activas (0.6)
    if es_activa is not None:
        es_activa = es_activa
