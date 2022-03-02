# Generated by Django 3.2 on 2022-02-27 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('nuevo', models.BooleanField()),
                ('fecha_fabricacion', models.DateTimeField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.marca')),
            ],
        ),
    ]