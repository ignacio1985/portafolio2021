from django.contrib import admin
from CORE.models import *

class EMPLEADO_ADMIN(admin.ModelAdmin):
    list_display=("rut_emp","nom_emp","appaterno_emp","apmaterno_emp","fk_perfil")

class PRODUCTO_ADMIN(admin.ModelAdmin):
    list_display=("nom_producto","fk_tipo_producto","precio")

class TICKET_ADMIN(admin.ModelAdmin):
    list_display=("codigo_ticket","fecha_imp","estado")

class BOLETA_ADMIN(admin.ModelAdmin):
    list_display=("num_boleta","fecha_boleta","valor_total")

class DETALLE_BOLETA_ADMIN(admin.ModelAdmin):
    list_display=("fk_num_boleta","fk_codigo_producto","cantidad")
class PEDIDO_TICKET_ADMIN(admin.ModelAdmin):
    list_display=("fk_num_ticket","fk_codigo_producto","cantidad")
class AUDITORIA_ADMIN(admin.ModelAdmin):
    list_display=("correlativo_aud","fecha_auditoria")

class DETALLE_AUDITORIA_ADMIN(admin.ModelAdmin):
    list_display=("fk_correlativo_aud","fk_codigo_emp")

class ERRORES_ADMIN(admin.ModelAdmin):
    list_display=("correlativo_error","fecha_error","nombre_modulo")

class INFORME_TICKET_ADMIN(admin.ModelAdmin):
    list_display=("correlativo_inf","fecha_informe","total_ventas")

admin.site.register(PERFIL)
admin.site.register(EMPRESA)
admin.site.register(TIPO_TICKET)
admin.site.register(DETALLE_AUDITORIA,DETALLE_AUDITORIA_ADMIN)
admin.site.register(AUDITORIA,AUDITORIA_ADMIN)
admin.site.register(TURNO)
admin.site.register(FORMA_PAGO)
admin.site.register(CAJERO)
admin.site.register(EMPLEADO,EMPLEADO_ADMIN)
admin.site.register(TICKET,TICKET_ADMIN)
admin.site.register(BOLETA,BOLETA_ADMIN)
admin.site.register(DETALLE_BOLETA,DETALLE_BOLETA_ADMIN)
admin.site.register(PEDIDO_TICKET,PEDIDO_TICKET_ADMIN)
admin.site.register(PRODUCTO,PRODUCTO_ADMIN)
admin.site.register(TIPO_PRODUCTO)
admin.site.register(ERRORES,ERRORES_ADMIN)
admin.site.register(INFORME_TICKET,INFORME_TICKET_ADMIN)
admin.site.register(SUCURSAL)