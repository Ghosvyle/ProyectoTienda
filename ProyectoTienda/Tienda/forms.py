from django import forms
from Tienda.models import empleado, cliente, producto, marca, pedido, comprobante, prod_pedido
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class empleadosForm(forms.ModelForm):

    class Meta:
        model= empleado
        fields = [
            'id_emp',
            'dni',
            'nombre',
            'apell_pat',
            'apell_mat'
        ]
        labels = {
            'id_emp': 'ID_Empleado',
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apell_pat': 'Apellido Paterno',
            'apell_mat': 'Apellido Materno',
        }
        widgets = {
            'id_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apell_pat': forms.TextInput(attrs={'class': 'form-control'}),
            'apell_mat': forms.TextInput(attrs={'class': 'form-control'}),
        }



class clientesForm(forms.ModelForm):

    class Meta:
        model = cliente
        fields = [
            'iden_cli',
            'nombre',
            'apell_pat',
            'apell_mat',
            'celular',
            'tipo'
        ]
        labels = {
            'iden_cli': 'ID_Usuario',
            'nombre': 'Nombre',
            'apell_pat': 'Apellido Paterno',
            'apell_mat': 'Apellido Materno',
            'celular': 'Celular',
            'tipo': 'Tipo',
        }
        widgets = {
            'iden_cli': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apell_pat': forms.TextInput(attrs={'class': 'form-control'}),
            'apell_mat': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }

class marcasForm(forms.ModelForm):

    class Meta:
        model = marca
        fields = [
            'id_marca',
            'nombre',
            'celular',
        ]
        labels = {
            'id_marca': 'ID_Marca',
            'nombre': 'Nombre',
            'celular': 'Celular',
        }
        widgets = {
            'id_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }

class productosForm(forms.ModelForm):

    class Meta:
        model = producto
        fields = [
            'id_producto',
            'id_marca',
            'talla',
            'precio',
            'estado'
        ]
        labels = {
            'id_producto': 'ID_Producto',
            'id_marca': 'ID_Marca',
            'talla': 'Talla',
            'precio': 'Precio',
            'estado': 'Estado',
        }
        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'id_marca': forms.Select(attrs={'class': 'form-control'}),
            'talla': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


class pedidosForm(forms.ModelForm):

    class Meta:
        model = pedido
        fields = [
            'id_pedido',
            'fecha',
            'igv',
            'monto',
            'id_emp',
            'iden_cli'
        ]
        labels = {
            'id_pedido': 'ID_Pedido',
            'fecha': 'Fecha',
            'igv': 'IGV',
            'monto': 'Monto',
            'id_emp': 'ID_Empleado',
            'iden_cli': 'ID_Cliente',
        }
        widgets = {
            'id_pedido': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'igv': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
            'id_emp': forms.Select(attrs={'class': 'form-control'}),
            'iden_cli': forms.Select(attrs={'class': 'form-control'}),
        }

class comprobantesForm(forms.ModelForm):

    class Meta:
        model = comprobante
        fields = [
            'id_comp',
            'tipo',
            'id_pedido',
            'iden_cli'
        ]
        labels = {
            'id_comp': 'ID_Comprobante',
            'tipo': 'Tipo',
            'id_pedido': 'ID_Pedido',
            'iden_cli': 'ID_Cliente',
        }
        widgets = {
            'id_comp': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'id_pedido': forms.Select(attrs={'class': 'form-control'}),
            'iden_cli': forms.Select(attrs={'class': 'form-control'}),
        }

class prodpedidosForm(forms.ModelForm):

    class Meta:
        model = prod_pedido
        fields = [
            'id_pro_ped',
            'id_pedido',
            'id_producto'
        ]
        labels = {
            'id_pro_ped': 'ID_Prod_Ped',
            'id_pedido': 'ID_Pedido',
            'id_producto': 'ID_Producto',
        }
        widgets = {
            'id_pro_ped': forms.TextInput(attrs={'class': 'form-control'}),
            'id_pedido': forms.Select(attrs={'class': 'form-control'}),
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }