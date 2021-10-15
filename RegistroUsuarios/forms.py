from django import forms
from .models import tipodocumento
from .models import Ciudad
from .models import Persona


class CiudadForm(forms.ModelForm):

	class Meta:
		model = Ciudad

		fields = [
			'nombre',
			'descripcion',
		
		]
		labels = {
			'nombre':'Nombre',
			'descripcion':'Descripcion',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','required':''}),    
		}
class TipoDocumentoForm(forms.ModelForm):

	class Meta:
		model = tipodocumento

		fields = [
			'nombre',
			'descripcion',
		
		]
		labels = {
			'nombre':'Nombre',
			'descripcion':'Descripcion',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','required':''}),    
		}
class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
			'nombre',
			'apellido',
			'idtipodocumento',
			'documento',
			'idlugarresiedencia',
			'fechadenacimiento',			
			'email',
			'telefono',
			'usuario',
			'contraseña',
			'confirmarcontraseña',
			'lugardenacimiento',	
		]
		labels = {
			'nombre':'Nombre',
			'apellido':'Apellido',
			'idtipodocumento':'Idtipodocumento',
			'documento':'Documento',
			'idlugarresiedencia':'Idlugarresidencia',
			'fechadenacimiento':'Fechadenacimiento',			
			'email':'Email',
			'telefono':'Telefono',
			'usuario':'Usuario',
			'contraseña':'Contraseña',
			'confirmarcontraseña':'Confirmarcontraseña',
			'lugardenacimiento':'Lugardenacimiento',	

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
			'apellido': forms.TextInput(attrs={'class':'form-control','required':''}),
			'idtipodocumento': forms.NumberInput(attrs={'class':'form-control','required':''}),
			'documento': forms.NumberInput(attrs={'class':'form-control','required':''}),
			'idlugarresidencia': forms.NumberInput(attrs={'class':'form-control','required':''}),
			'fechadenacimiento': forms.DateInput(attrs={'class':'form-control','required':''}),
			'telefono': forms.NumberInput(attrs={'class':'form-control','required':''}),
			'usuario': forms.TextInput(attrs={'class':'form-control','required':''}),
			'contraseña': forms.PasswordInput(attrs={'class':'form-control','required':''}),
			'confirmarcontraseña': forms.PasswordInput(attrs={'class':'form-control','required':''}),
			'lugardenacimiento': forms.TextInput(attrs={'class':'form-control','required':''}),            
		}

