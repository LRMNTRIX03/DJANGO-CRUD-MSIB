# Generated by Django 4.2.16 on 2024-11-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='harga',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='barang',
            name='nama_barang',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='barang',
            name='stok',
            field=models.IntegerField(max_length=3),
        ),
    ]
