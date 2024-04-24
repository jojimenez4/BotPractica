from django import forms
from .models import *


class UsuarioForm(forms.ModelForm):
    Comuna_Usuario = forms.ModelChoiceField(queryset=Comuna.objects.all(), empty_label="Seleccione una opción", widget=forms.Select(attrs={'class': 'form-control'}))
    Genero_Usuario = forms.ModelChoiceField(queryset=Genero.objects.all(), empty_label="Seleccione una opción", widget=forms.Select(attrs={'class': 'form-control'}))
    SistemaSalud_Usuario = forms.ModelChoiceField(queryset=SistemaSalud.objects.all(), empty_label="Seleccione una opción", widget=forms.Select(attrs={'class': 'form-control'}))
    Ocupacion_Usuario = forms.ModelChoiceField(queryset=Ocupacion.objects.all(), empty_label="Seleccione una opción", widget=forms.Select(attrs={'class': 'form-control'}))
    AnioNacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'dark-input'}))
    Rut = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Whatsapp = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['AnioNacimiento', 'Rut', 'Whatsapp', 'Comuna_Usuario', 'Genero_Usuario', 'SistemaSalud_Usuario', 'Ocupacion_Usuario']

    def clean_Comuna_Usuario(self):
        comuna = self.cleaned_data['Comuna_Usuario']
        return comuna

    def clean_Genero_Usuario(self):
        genero = self.cleaned_data['Genero_Usuario']
        return genero

    def clean_SistemaSalud_Usuario(self):
        sistema_salud = self.cleaned_data['SistemaSalud_Usuario']
        return sistema_salud

    def clean_Ocupacion_Usuario(self):
        ocupacion = self.cleaned_data['Ocupacion_Usuario']
        return ocupacion

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['pregunta']
        
class MensajeContenidoForm(forms.ModelForm):
    class Meta:
        model = MensajeContenido
        fields = ['texto', 'Genero_Usuario', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'dark-input'})
        }