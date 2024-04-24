# Generated by Django 5.0.1 on 2024-01-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0020_rename_id_manychat_usuariorespuesta_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Comuna'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Genero'),
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Ocupacion'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Pregunta'),
        ),
        migrations.AlterField(
            model_name='preguntaopcionrespuesta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Opcion Respuesta'),
        ),
        migrations.AlterField(
            model_name='sistemasalud',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Sistema Salud'),
        ),
        migrations.AlterField(
            model_name='usuariorespuesta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Usuario Respuesta'),
        ),
    ]
