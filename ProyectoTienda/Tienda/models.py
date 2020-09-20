from django.db import models

# Create your models here.
class empleado(models.Model):
    id_emp= models.CharField(max_length=10)
    dni = models.CharField(max_length=8)
    nombre= models.CharField(max_length=20)
    apell_pat= models.CharField(max_length=20)
    apell_mat= models.CharField(max_length=20)
    def __str__(self):
        return self.id_emp +" "+ self.dni +" "+ self.nombre +" "+ self.apell_pat +" "+ self.apell_mat

class usuario(models.Model):
    id_usuario=models.CharField(max_length=10)
    nom_user=models.CharField(max_length=20)
    clave=models.CharField(max_length=10)
    id_emp=models.ForeignKey(empleado,on_delete=models.CASCADE)

class cliente(models.Model):
    iden_cli= models.CharField(max_length=10)
    nombre= models.CharField(max_length=20)
    apell_pat= models.CharField(max_length=20)
    apell_mat= models.CharField(max_length=20)
    celular= models.CharField(max_length=9)
    NATURAL= 'Natural'
    JURIDICA= 'Juridica'
    TIPO = ((NATURAL, 'Natural'),(JURIDICA, 'Juridica'))
    tipo= models.CharField(max_length=8, choices=TIPO)
    def __str__(self):
        return self.iden_cli +" "+ self.nombre +" "+ self.apell_pat +" "+ self.apell_mat +" "+ self.celular
        +" "+ self.tipo

class marca(models.Model):
    id_marca= models.CharField(max_length=20)
    nombre= models.CharField(max_length=20)
    celular= models.CharField(max_length=9)
    def __str__(self):
        return self.id_marca +" "+ self.nombre +" "+ self.celular

class producto(models.Model):
    id_producto= models.CharField(max_length=8)
    id_marca= models.ForeignKey(marca, on_delete=models.CASCADE)
    tipo= models.CharField(max_length=20)
    XS='Extra Small'
    S='Small'
    M='Medium'
    L='Large'
    XL='Extra Large'
    XXL='2 Extra Large'
    TALLA=((XS,'Extra Small'),(S,'Small'),(M,'Medium'),(L,'Large'),(XL,'Extra Large'),(XXL,'2 Extra Large'))
    talla=models.CharField(max_length=20, choices=TALLA)
    precio= models.IntegerField()
    DISPONIBLE='Disponible'
    NODISPONIBLE='No Disponible'
    ESTADO=((DISPONIBLE,'Disponible'),(NODISPONIBLE,'No Disponible'))
    estado=models.CharField(max_length=20, choices=ESTADO)
    stock=models.IntegerField(null=True)
    def __str__(self):
        return self.id_producto +" "+ str(self.id_marca.id_marca) +" "+ self.tipo +" "+ self.talla +" "+ str(self.precio) +" "+ self.estado

class pedido(models.Model):
    id_pedido=models.CharField(max_length=20)
    fecha=models.DateField()
    igv=models.IntegerField()
    monto=models.IntegerField()
    monto_igv=models.IntegerField(null=True)
    id_emp=models.ForeignKey(empleado,on_delete=models.CASCADE)
    iden_cli=models.ForeignKey(cliente,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_pedido +" "+ str(self.fecha) +" "+ str(self.igv) +" "+ str(self.monto) + str(self.monto_igv) +" "+ str(self.id_emp.id_emp) +" "+ str(self.iden_cli.iden_cli)
    

class comprobante(models.Model):
    id_comp=models.CharField(max_length=20)
    BOLETA='Boleta'
    FACTURA='Factura'
    TIPO=((BOLETA,'Boleta'),(FACTURA,'Factura'))
    tipo=models.CharField(max_length=10, choices=TIPO)
    id_pedido=models.ForeignKey(pedido,on_delete=models.CASCADE)
    iden_cli=models.ForeignKey(cliente,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_comp +" "+ self.tipo +" "+ str(self.id_pedido.id_pedido)+ " " + str(self.iden_cli.iden_cli)

class prod_pedido(models.Model):
    id_pro_ped=models.CharField(max_length=10)
    cantidad=models.IntegerField(null=True)
    id_pedido=models.ForeignKey(pedido,on_delete=models.CASCADE)
    id_producto=models.ForeignKey(producto,on_delete=models.CASCADE)
    def __str__(self):
        return self.id_pro_ped + " " + str(self.id_pedido.id_pedido) +" "+ str(self.id_producto.id_producto)

class historial(models.Model):
    old_ident_cli=models.CharField(max_length=10)
    new_ident_cli=models.CharField(max_length=10)
    old_celular=models.CharField(max_length=9)
    new_celular=models.CharField(max_length=9)
    user_action=models.TextField()
    create_at=models.TextField()

