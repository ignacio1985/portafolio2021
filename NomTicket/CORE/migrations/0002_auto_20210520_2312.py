# Generated by Django 3.1.4 on 2021-05-21 03:12

from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='clave',
            field=fernet_fields.fields.EncryptedCharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_empresa',
            field=models.ForeignKey(help_text='Empresa', on_delete=django.db.models.deletion.PROTECT, to='CORE.empresa'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_perfil',
            field=models.ForeignKey(help_text='Perfil', on_delete=django.db.models.deletion.PROTECT, to='CORE.perfil'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fk_turno',
            field=models.ForeignKey(help_text='Turno', on_delete=django.db.models.deletion.PROTECT, to='CORE.turno'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='saldo',
            field=models.PositiveIntegerField(null=True, verbose_name='cargar saldo'),
        ),
    ]