# Generated by Django 5.0.1 on 2024-02-15 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0027_mitabla'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitabla',
            name='Genero_Usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='botApp.genero'),
            preserve_default=False,
        ),
    ]
