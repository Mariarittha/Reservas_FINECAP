# Generated by Django 4.2.4 on 2023-09-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=150)),
                ('nome_empresa', models.CharField(max_length=150)),
                ('categoria_empresa', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=150)),
                ('valor', models.FloatField()),
            ],
        ),
    ]