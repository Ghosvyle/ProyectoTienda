# Generated by Django 3.0.8 on 2020-07-21 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iden_cli', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apell_pat', models.CharField(max_length=20)),
                ('apell_mat', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=9)),
                ('tipo', models.CharField(choices=[('Natural', 'Natural'), ('Juridica', 'Juridica')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_emp', models.CharField(max_length=10)),
                ('dni', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=20)),
                ('apell_pat', models.CharField(max_length=20)),
                ('apell_mat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_marca', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('igv', models.IntegerField()),
                ('monto', models.IntegerField()),
                ('id_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.empleado')),
                ('iden_cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.CharField(max_length=10)),
                ('nom_user', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=10)),
                ('id_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.CharField(max_length=8)),
                ('tipo', models.CharField(max_length=20)),
                ('talla', models.CharField(choices=[('Extra Small', 'Extra Small'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large'), ('2 Extra Large', '2 Extra Large')], max_length=20)),
                ('precio', models.IntegerField()),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No Disponible')], max_length=20)),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.marca')),
            ],
        ),
        migrations.CreateModel(
            name='prod_pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pro_ped', models.CharField(max_length=10)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.producto')),
            ],
        ),
        migrations.CreateModel(
            name='comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_comp', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[('Boleta', 'Boleta'), ('Factura', 'Factura')], max_length=10)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.pedido')),
                ('iden_cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.cliente')),
            ],
        ),
    ]
