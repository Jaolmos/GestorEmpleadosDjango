# Generated by Django 3.2.5 on 2021-08-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_alter_empleado_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=140, verbose_name='Nombre completo'),
        ),
    ]