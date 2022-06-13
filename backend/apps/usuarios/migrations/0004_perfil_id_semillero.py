# Generated by Django 4.0.4 on 2022-06-13 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0001_initial'),
        ('usuarios', '0003_perfil_año_i_perfil_direccion_perfil_f_grado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='id_semillero',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='semilleros.semillero'),
            preserve_default=False,
        ),
    ]
