# Generated by Django 3.1.4 on 2021-07-08 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0003_auto_20210523_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='clave',
            field=models.CharField(max_length=100, verbose_name='contraseña'),
        ),
        migrations.CreateModel(
            name='PRODUCTO_TURNO',
            fields=[
                ('id_producto_turno', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.tipo_producto')),
                ('fk_id_turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.turno')),
            ],
            options={
                'verbose_name': 'producto_turno',
                'verbose_name_plural': 'producto_turnos',
                'db_table': 'PRODUCTO_TURNO',
            },
        ),
    ]
