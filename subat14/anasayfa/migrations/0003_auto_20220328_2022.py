# Generated by Django 3.2.12 on 2022-03-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0002_bilgi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bilgi',
            name='ogrenci_bilgi',
        ),
        migrations.AddField(
            model_name='bilgi',
            name='aciklama',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bilgi',
            name='isim',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
