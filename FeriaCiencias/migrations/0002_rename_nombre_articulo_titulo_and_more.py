# Generated by Django 4.2.13 on 2024-06-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeriaCiencias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='nombre',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='seccion',
            old_name='nombre',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='titulo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]