# Generated by Django 5.0.1 on 2024-01-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0023_usuariotextopregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Referencia',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
