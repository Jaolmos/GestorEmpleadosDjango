# Generated by Django 3.2.5 on 2021-07-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_rename_fieldname_empleado_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('1', 'Informatico'), ('2', 'Administrador'), ('3', 'Economista'), ('4', 'Otro')], max_length=60, verbose_name='Trabajo'),
        ),
    ]