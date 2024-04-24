from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone



class Comuna(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Comuna")
    Nombre_Comuna = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_Comuna


class Genero(models.Model):
    FEMENINO = "Femenino"
    MASCULINO = "Masculino"
    OTRO = "Otro"

    GENERO_CHOICES = [
        (FEMENINO, "Femenino"),
        (MASCULINO, "Masculino"),
        (OTRO, "Otro"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID Genero")
    OPC_Genero = models.CharField(max_length=50, choices=GENERO_CHOICES)

    def __str__(self):
        return self.OPC_Genero


class SistemaSalud(models.Model):
    FONASA = "Fonasa"
    ISAPRE = "Isapre"
    OTRO = "Otro"

    SISTEMA_SALUD_CHOICES = [
        (FONASA, "Fonasa"),
        (ISAPRE, "Isapre"),
        (OTRO, "Otro"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID Sistema Salud")
    OPC_SistemaSalud = models.CharField(max_length=50, choices=SISTEMA_SALUD_CHOICES)

    def __str__(self):
        return self.OPC_SistemaSalud


class Ocupacion(models.Model):
    DUENIACASA = "Dueña de Casa"
    TRABAJADOR = "Trabajadora"
    OTRO = "Otro"

    OCUPACION_CHOICES = [
        (DUENIACASA, "Dueña de Casa"),
        (TRABAJADOR, "Trabajadora"),
        (OTRO, "Otro"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID Ocupacion")
    OPC_Ocupacion = models.CharField(max_length=50, choices=OCUPACION_CHOICES)

    def __str__(self):
        return self.OPC_Ocupacion


class Usuario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Usuario")
    AnioNacimiento = models.CharField(max_length=200, verbose_name="Fecha de Nacimiento")
    id_manychat = models.CharField(max_length=200)
    Rut = models.CharField(max_length=10)
    Whatsapp = models.CharField(max_length=200)
    Referencia = models.CharField(max_length=200)
    Comuna_Usuario = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    Genero_Usuario = models.ForeignKey(Genero, on_delete=models.CASCADE)
    SistemaSalud_Usuario = models.ForeignKey(SistemaSalud, on_delete=models.CASCADE)
    Ocupacion_Usuario = models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    Fecha_Ingreso = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


class Pregunta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Pregunta")
    pregunta = models.CharField(max_length=200)

    def __str__(self):
        return self.pregunta


class PreguntaOpcionRespuesta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Opcion Respuesta")
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    OPC_Respuesta = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id_pregunta} - {self.OPC_Respuesta}"

class UsuarioRespuesta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Usuario Respuesta")
    Rut = models.CharField(max_length=10)
    id_opc_respuesta = models.ForeignKey(PreguntaOpcionRespuesta, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Rut} - {self.id_opc_respuesta}"

class UsuarioTextoPregunta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Texto Pregunta")
    Rut = models.CharField(max_length=10)
    texto_pregunta = models.CharField(max_length=200)
    fecha_pregunta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Rut} - {self.texto_pregunta}"


class MensajeContenido(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Texto")
    texto = models.CharField(max_length=200)
    Genero_Usuario = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha")


