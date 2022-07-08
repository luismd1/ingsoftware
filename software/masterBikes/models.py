from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User
# Crea tus modelos aquí.
pagos = [('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta')]
class Bici(models.Model):
    idBici = models.AutoField(primary_key = True, verbose_name = "Id de la bici")
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre de la bici")
    marca = models.CharField(max_length = 50, verbose_name = "Marca de la bici")
    modelo = models.CharField(max_length = 50, verbose_name = "Modelo de la bici")
    color = models.CharField(max_length = 50, verbose_name = "Color de la bici")
    precio = models.IntegerField(verbose_name = "Precio de la bici")
    cantidad = models.IntegerField(verbose_name = "Cantidad de bicis")
    descripcion = models.CharField(max_length = 50, verbose_name = "Descripcion de la bici")
    imagen = models.ImageField(upload_to = 'bicis', null = True, verbose_name = "Imagen de la bici")
    
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    idVenta = models.AutoField(primary_key = True, verbose_name = "Id de la venta")
    idBici = models.ForeignKey(Bici, on_delete = models.CASCADE, verbose_name = "Id de la bici")
    cliente = UserForeignKey(auto_user_add=True, verbose_name = "cliente")
    fecha = models.DateField(verbose_name = "Fecha de la venta")
    fechaTermino = models.DateField(verbose_name = "Fecha de termino de la venta")
    formadepago = models.CharField(max_length = 50, verbose_name = "Forma de pago", choices = pagos)
    cantidad = models.IntegerField(verbose_name = "Cantidad de bicis")
    precio = models.IntegerField(verbose_name = "Precio de la venta")

class Reparacion(models.Model):
    idReparacion = models.AutoField(primary_key = True, verbose_name = "Id de la reparacion")
    idBici = models.ForeignKey(Bici, on_delete = models.CASCADE, verbose_name = "Id de la bici")
    cliente = UserForeignKey(auto_user_add = True, verbose_name="cliente")
    fecha = models.DateField(auto_now_add = True, verbose_name = "Fecha de la reparacion")
    precio = models.IntegerField(verbose_name = "Precio de la reparacion")
    estado = models.CharField(max_length = 50, verbose_name = "Estado de la reparacion")

class Promocion(models.Model):
    idPromocion = models.AutoField(primary_key = True, verbose_name = "Id de la promocion")
    Bicis = models.ForeignKey(Bici, on_delete = models.CASCADE, verbose_name = "la bici")
    cantidad = models.IntegerField(verbose_name = "Cantidad de bicis")
    
    def __str__(self):
        return self.idPromocion

class Despacho(models.Model):
    idDespacho = models.AutoField(primary_key = True, verbose_name = "Id del despacho")
    idVenta = models.ForeignKey(Venta, on_delete = models.CASCADE, verbose_name = "Id de la venta")
    fecha = models.DateField(auto_now_add = True, verbose_name = "Fecha del despacho")
    fechaTermino = models.DateField(null = True, verbose_name = "Fecha de termino del despacho") 
    estado = models.CharField(max_length = 50, verbose_name = "Estado del despacho")
    direccion = models.CharField(max_length = 50, verbose_name = "Direccion del despacho")
    cliente = UserForeignKey(auto_user_add = True, verbose_name = "cliente")
    
    def __str__(self):
        return self.idDespacho