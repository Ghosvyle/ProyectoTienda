# Generated by Django 3.0.8 on 2020-09-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_historial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='monto_igv',
            field=models.IntegerField(null=True),
        ),
    ]
