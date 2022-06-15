# Generated by Django 4.0.4 on 2022-06-15 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semilleros', '0006_remove_semillero_id_users'),
        ('usuarios', '0009_remove_perfil_id_semillero'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='id_semillero',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to='semilleros.semillero'),
            preserve_default=False,
        ),
    ]