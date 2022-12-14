# Generated by Django 4.1 on 2022-08-31 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('num_telefono', models.IntegerField()),
                ('estado_civil', models.CharField(max_length=50)),
                ('hijos', models.IntegerField()),
                ('trabajo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('año_vehiculo', models.IntegerField()),
                ('patente', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
                ('dueño_vehiculo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('largo_terreno', models.FloatField()),
                ('ancho_terreno', models.FloatField()),
                ('largo_casa', models.FloatField()),
                ('ancho_casa', models.FloatField()),
                ('titular_terreno', models.CharField(max_length=50)),
                ('cant_personas_en_casa', models.IntegerField()),
            ],
        ),
    ]
