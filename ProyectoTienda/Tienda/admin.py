from django.contrib import admin
from Tienda.models import empleado, usuario, cliente, marca, producto, pedido, comprobante, prod_pedido

admin.site.register(empleado)
admin.site.register(usuario)
admin.site.register(cliente)
admin.site.register(marca)
admin.site.register(producto)
admin.site.register(pedido)
admin.site.register(comprobante)
admin.site.register(prod_pedido)

