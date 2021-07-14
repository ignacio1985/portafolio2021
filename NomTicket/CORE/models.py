from django.db import models

class TIPO_PRODUCTO(models.Model):
    id_tipo_producto = models.AutoField(primary_key=True)   #clave primaria
    nom_tipo_producto = models.CharField("nombre categoria",max_length=30,null=False)

    class Meta:
        verbose_name = "tipo producto"
        verbose_name_plural = "tipo productos"
        db_table = "TIPO_PRODUCTO"

    def __str__(self):
        return self.nom_tipo_producto
#**************************************************************************************************************
class PRODUCTO(models.Model):
    codigo_producto = models.AutoField(primary_key=True)    #clave primaria
    nom_producto = models.CharField("nombre producto",max_length=30,null=False,blank=False)
    descripcion = models.TextField("descripcion",max_length=100,null=False, blank=False)
    precio = models.PositiveIntegerField("precio $")
    fk_tipo_producto = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.PROTECT,null=False)

    class Meta:
        verbose_name ="producto"
        verbose_name_plural ="productos"
        db_table = "PRODUCTO"
    
    def __str__(self):
        return f"{self.nom_producto},{self.fk_tipo_producto},{self.precio}"
#**************************************************************************************************************
class TIPO_TICKET(models.Model):
    id_tipo_ticket = models.AutoField(primary_key=True)     #clave primaria
    descripcion = models.CharField("tipo ticket",null=False,blank=False,max_length=30)

    class Meta:
        verbose_name ="tipo de ticket"
        verbose_name_plural ="tipos de tickets"
        db_table = "TIPO_TICKET"
    
    def __str__(self):
        return self.descripcion

#**************************************************************************************************************
class PERFIL(models.Model):
    id_perfil = models.AutoField(primary_key=True)      #clave primaria
    nombre_perfil = models.CharField("nombre prefil",null=False,blank=False,max_length=30)
    ticket_diario = models.PositiveIntegerField("cantidad de tickets diarios",null=False,default=1)
    valor_desayuno = models.IntegerField("valor desayuno",null=False)
    valor_almuerzo = models.IntegerField("valor almuerzo",null=False)
    valor_once = models.IntegerField("valor once",null=False)
    valor_cena = models.IntegerField("valor cena",null=False)
    bonificacion = models.PositiveIntegerField("bonificacion",null=False,default=0)    

    class Meta:
        verbose_name ="perfil"
        verbose_name_plural="perfiles"
        db_table = "PERFIL"

    def __str__(self):
        return self.nombre_perfil
#**************************************************************************************************************
class TURNO(models.Model):
    id_turno = models.AutoField(primary_key=True)   #Clave primaria
    nombre = models.CharField("nombre turno",null=False,blank=False,max_length=30)
    hora_inicio = models.CharField("hora inicio",max_length=5,null=False,blank=False)
    hora_termino = models.CharField("hora termino",max_length=5,null=False,blank=False)

    class Meta:
        verbose_name ="turno"
        verbose_name_plural="turnos"
        db_table ="TURNO"
    
    def __str__(self):
        return self.nombre
#**************************************************************************************************************
class EMPRESA(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField("nombre empresa",max_length=30,null=False,blank=False)

    class Meta:
        verbose_name ="empresa"
        verbose_name_plural ="empresas"
        db_table="EMPRESA"

    def __str__(self):
        return self.nombre_empresa
#**************************************************************************************************************
valores = (
    (264000,"Administración 264000"),
    (378000,"Jefaturas 378000"),
    (450000,"Gerente 450000"),
    (276000,"Operarios 276000"),
)
class EMPLEADO(models.Model):
    codigo_emp = models.AutoField(primary_key=True)         
    rut_emp = models.CharField("rut empleado (sin puntos con guion)",max_length=10,null=False,blank=False)     #clave primaria
    nom_emp = models.CharField("nombre",max_length=30,null=False,blank=False)
    appaterno_emp = models.CharField("apellido paterno",max_length=30,null=False,blank=False)
    apmaterno_emp = models.CharField("apellido materno",max_length=30,null=False,blank=False)
    clave = models.CharField("contraseña",max_length=100,null=False,blank=False)
    saldo = models.PositiveIntegerField("cargar saldo",choices=valores, default=0)
    email = models.EmailField("email empleado",max_length=100,null=True,blank=False)
    fk_empresa = models.ForeignKey(EMPRESA,on_delete=models.PROTECT,null=False,verbose_name="Empresa")
    fk_perfil = models.ForeignKey(PERFIL,on_delete=models.PROTECT,null=False,verbose_name="Perfil")
    fk_turno = models.ForeignKey(TURNO,on_delete=models.PROTECT,null=False,verbose_name="Turno")

    class Meta:
        verbose_name ="empleado"
        verbose_name_plural="empleados"
        db_table = "EMPLEADO"
    
    def __str__(self):
        return f"{self.rut_emp},{self.nom_emp},{self.appaterno_emp},{self.apmaterno_emp},{self.fk_perfil}"
#**************************************************************************************************************
class VISITANTE(models.Model):
    rut_visitante = models.CharField("rut visitante (sin puntos con guion",primary_key=True,null=False,blank=False,max_length=10) #clave primaria
    nombre = models.CharField("nombre",null=False,blank=False,max_length=50)
    apellido = models.CharField("apellido",null=False,blank=False,max_length=50)
    email = models.EmailField(max_length=100,null=True,blank=False)
    description = models.TextField("descripcion",null=True,max_length=255)

    class Meta:
        verbose_name = 'visitante'
        verbose_name_plural = 'visitantes'
        db_table = 'VISITANTE'

    def __str__(self):
        return f"{self.rut_visitante},{self.nombre}"
#**************************************************************************************************************
class TICKET(models.Model):
    codigo_ticket = models.AutoField(primary_key=True)
    fecha_imp = models.DateField("fecha impresion",auto_now=False,auto_now_add=True,null=False)
    hora_vig_inicio = models.CharField("hora inicio",max_length=5,null=False,blank=False)
    hora_vig_termino = models.CharField("hora termino",max_length=5,null=False,blank=False)
    estado = models.BooleanField("estado del ticket",default=True)
    valor = models.PositiveIntegerField("valor ticket")
    comentario = models.TextField("comentario",null=True,blank=True,max_length=100)
    fk_codigo_emp = models.ForeignKey(EMPLEADO,on_delete=models.PROTECT,null=True)
    fk_rut_visitante = models.ForeignKey(VISITANTE,on_delete=models.PROTECT,null=True) 
    fk_tipo_ticket = models.ForeignKey(TIPO_TICKET,on_delete=models.PROTECT,null=False)

    class Meta:
        verbose_name ="ticket"
        verbose_name_plural="tickets"
        db_table = "TICKET"
    
    def __str__(self):
        return f"{self.codigo_ticket},{self.fecha_imp},{self.estado}"
#**************************************************************************************************************
class SUCURSAL(models.Model):
    id_sucursal = models.AutoField(primary_key=True)    #clave primaria 
    nombre_sucursal = models.CharField("nombre sucursal",max_length=50,null=False,blank=False)
    direccion_sucursal = models.CharField("direccion sucursal",max_length=150,null=False,blank=False)

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural ="sucursales"
        db_table ="SUCURSAL"

    def __str__(self):
        return self.nombre_sucursal
#**************************************************************************************************************
class CAJERO(models.Model):
    rut_cajero = models.CharField("rut cajero",primary_key=True,null=False,blank=False,max_length=10)  #clave primaria
    nombre = models.CharField("nombre cajero",max_length=30,null=False,blank=False)
    clave = models.CharField("contraseña",max_length=50,null=False,blank=False)
    estado = models.BooleanField("habilitado",null=False,default=False)
    administrador = models.BooleanField("Administrador",null=False,default=False)
    fk_sucursal = models.ForeignKey(SUCURSAL,on_delete=models.PROTECT,null=False)

    class Meta:
        verbose_name ="cajero"
        verbose_name_plural ="cajeros"
        db_table ="CAJERO"
    
    def __str__(self):
        return self.nombre
#**************************************************************************************************************
class FORMA_PAGO(models.Model):
    id_forma_pago = models.AutoField(primary_key=True)  #clave primaria
    nombre_forma_pago = models.CharField(max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = "forma de pago"
        verbose_name_plural = "formas de pago"
        db_table ="FORMAS_PAGO"
    
    def __str__(self):
        return self.nombre_forma_pago
#**************************************************************************************************************
class BOLETA(models.Model):
    num_boleta = models.AutoField(primary_key=True)     #clave primaria
    fecha_boleta = models.DateField("fecha emision",auto_now=False,auto_now_add=True)
    hora_venta = models.CharField("hora venta",max_length=5,null=False,blank=False)
    valor_total = models.PositiveIntegerField("total")
    valor_ticket = models.PositiveIntegerField("valor ticket")
    saldo_por_pagar = models.PositiveIntegerField("saldo por pagar",null=True,default=0)
    fk_codigo_ticket = models.ForeignKey(TICKET,on_delete=models.PROTECT,null=True)
    fk_forma_pago = models.ForeignKey(FORMA_PAGO,on_delete=models.PROTECT,null=False)
    fk_rut_cajero = models.ForeignKey(CAJERO,on_delete=models.PROTECT,null=False)

    class Meta:
        verbose_name ="boleta"
        verbose_name_plural="boletas"
        db_table ="BOLETA"

    def __str__(self):
        return f"{self.num_boleta},{self.fecha_boleta},{self.valor_total}"
#**************************************************************************************************************
class DETALLE_BOLETA(models.Model):
    fk_num_boleta = models.ForeignKey(BOLETA,on_delete=models.PROTECT,null=False)
    fk_codigo_producto = models.ForeignKey(PRODUCTO,on_delete=models.PROTECT,null=False)
    cantidad = models.PositiveIntegerField("cantidad")

    class Meta:
        verbose_name = "detalle boleta"
        verbose_name_plural = "detalles boletas"
        db_table="DETALLE_BOLETA"

    def __str__(self):
        return f"{self.fk_num_boleta},{self.fk_codigo_producto},{self.cantidad}"
#**************************************************************************************************************
#**************************************************************************************************************
class PEDIDO_TICKET(models.Model):
    fk_num_ticket = models.ForeignKey(TICKET,on_delete=models.PROTECT,null=False)
    fk_codigo_producto = models.ForeignKey(PRODUCTO,on_delete=models.PROTECT,null=False)
    cantidad = models.PositiveIntegerField("cantidad")

    class Meta:
        verbose_name = "pedido ticket"
        verbose_name_plural = "pedidos tickets"
        db_table="PEDIDO_TICKET"

    def __str__(self):
        return f"{self.fk_num_ticket},{self.fk_codigo_producto},{self.cantidad}"
#**************************************************************************************************************
class AUDITORIA(models.Model):
    correlativo_aud = models.AutoField(primary_key=True)    #clave primaria
    fecha_auditoria = models.DateField("fecha auditoria",auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name ="auditoria"
        verbose_name_plural="auditorias"
        db_table ="AUDITORIA"
    
    def __str__(self):
        return f"{self.correlativo_aud},{self.fecha_auditoria}"
#**************************************************************************************************************
class DETALLE_AUDITORIA(models.Model):
    fk_correlativo_aud = models.ForeignKey(AUDITORIA,on_delete=models.PROTECT,null=False)
    fk_codigo_emp = models.ForeignKey(EMPLEADO,on_delete=models.PROTECT,null=False)
    fecha_no_uso = models.DateField("fecha no uso",null=False)

    class Meta:
        verbose_name = "detalle auditoria"
        verbose_name_plural ="detalle auditorias"
        db_table ="DETALLE_AUDITORIA"

    def __str__(self):
        return f"{self.fk_correlativo_aud},{self.fk_codigo_emp}"
#**************************************************************************************************************
class ERRORES(models.Model):
    correlativo_error = models.AutoField(primary_key=True)      #clave primaria 
    fecha_error = models.DateField("fecha error",auto_now=False,auto_now_add=True,null=False)
    nombre_modulo = models.CharField("nombre modulo",max_length=150,null=False,blank=False)
    descripcion_error = models.CharField("descripcion error",max_length=200,null=False,blank=False)

    class Meta:
        verbose_name ="error"
        verbose_name_plural ="errores"
        db_table="ERRORES"
    
    def __str__(self):
        return f"{self.correlativo_error},{self.fecha_error},{self.nombre_modulo}"

#**************************************************************************************************************
class INFORME_TICKET(models.Model):
    correlativo_inf = models.AutoField(primary_key=True)    #clave primaria
    fecha_informe = models.DateField("fecha informe",auto_now=False,auto_now_add=True,null=False)
    fecha_inicio = models.DateField("fecha inicio",auto_now=False,auto_now_add=True,null=False)
    fecha_termino = models.DateField("fecha termino",auto_now=False,auto_now_add=True,null=False)
    tipo_servicio = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.PROTECT,null=True)
    cant_boletas = models.PositiveIntegerField("cantidad de boletas")
    cant_tickets = models.PositiveIntegerField("cantidad de tickets")
    total_ventas = models.PositiveIntegerField("total de ventas")

    class Meta:
        verbose_name ="informe ticket"
        verbose_name_plural="informes tickets"
        db_table="INFORME_TICKET"
    
    def __str__(self)        :
        return f"{self.correlativo_inf},{self.fecha_informe},{self.total_ventas}"
#***************************************************************************************************************
class PRODUCTO_TURNO(models.Model):
    id_producto_turno = models.AutoField(primary_key=True)
    fk_id_tipo_producto = models.ForeignKey(TIPO_PRODUCTO,on_delete=models.PROTECT,null=False)
    fk_id_turno = models.ForeignKey(TURNO,on_delete=models.PROTECT,null=False)    

    class Meta:
        verbose_name = 'producto_turno'
        verbose_name_plural = 'producto_turnos'
        db_table = 'PRODUCTO_TURNO'

    def __str__(self):
        return f"{self.fk_id_tipo_producto},{self.fk_id_turno}"
#***************************************************************************************************************