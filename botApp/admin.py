from django.contrib import admin
from .models import *


class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "id_manychat",
        "Rut",
        "Whatsapp",
        "Referencia",
        "AnioNacimiento",
        "Comuna_Usuario",
        "Genero_Usuario",
        "SistemaSalud_Usuario",
        "Ocupacion_Usuario",
        "Fecha_Ingreso",
    )
    search_fields = (
        "id",
        "id_manychat",
        "Rut",
        "Whatsapp",
        "Referencia",
        "AnioNacimiento",
        "Comuna_Usuario",
        "Genero_Usuario",
        "SistemaSalud_Usuario",
        "Ocupacion_Usuario",
        "Fecha_Ingreso",
    )
    list_filter = (
        "id",
        "id_manychat",
        "Rut",
        "Whatsapp",
        "Referencia",
        "AnioNacimiento",
        "Comuna_Usuario",
        "Genero_Usuario",
        "SistemaSalud_Usuario",
        "Ocupacion_Usuario",
        "Fecha_Ingreso",
    )


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "pregunta")
    search_fields = ("id", "pregunta")
    list_filter = ("id", "pregunta")


class UsuarioRespuestaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "Rut",
        "id_opc_respuesta",
        "fecha_respuesta",
    )
    search_fields = (
        "id",
        "Rut",
        "id_opc_respuesta",
        "fecha_respuesta",
    )
    list_filter = (
        "id",
        "Rut",
        "id_opc_respuesta",
        "fecha_respuesta",
    )


class PreguntaOpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ("id", "id_pregunta", "OPC_Respuesta")
    search_fields = ("id", "id_pregunta", "OPC_Respuesta")
    list_filter = ("id", "id_pregunta", "OPC_Respuesta")


class ComunaAdmin(admin.ModelAdmin):
    list_display = ("id", "Nombre_Comuna")
    search_fields = ("id", "Nombre_Comuna")
    list_filter = ("id", "Nombre_Comuna")


class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "OPC_Genero")
    search_fields = ("id", "OPC_Genero")
    list_filter = ("id", "OPC_Genero")


class SistemaSaludAdmin(admin.ModelAdmin):
    list_display = ("id", "OPC_SistemaSalud")
    search_fields = ("id", "OPC_SistemaSalud")
    list_filter = ("id", "OPC_SistemaSalud")


class OcupacionAdmin(admin.ModelAdmin):
    list_display = ("id", "OPC_Ocupacion")
    search_fields = ("id", "OPC_Ocupacion")
    list_filter = ("id", "OPC_Ocupacion")


class UsuarioTextoPreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "Rut", "texto_pregunta", "fecha_pregunta")
    search_fields = ("id", "Rut", "texto_pregunta", "fecha_pregunta")
    list_filter = ("id", "Rut", "texto_pregunta", "fecha_pregunta")
    
class MensajeContenidoAdmin(admin.ModelAdmin):
    list_display = ("id", "texto", "Genero_Usuario","fecha")
    search_fields = ("id", "texto", "fecha", "Genero_Usuario")
    list_filter = ("id", "texto", "fecha", "Genero_Usuario")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(UsuarioRespuesta, UsuarioRespuestaAdmin)
admin.site.register(PreguntaOpcionRespuesta, PreguntaOpcionRespuestaAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(SistemaSalud, SistemaSaludAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(UsuarioTextoPregunta, UsuarioTextoPreguntaAdmin)
admin.site.register(MensajeContenido, MensajeContenidoAdmin)
