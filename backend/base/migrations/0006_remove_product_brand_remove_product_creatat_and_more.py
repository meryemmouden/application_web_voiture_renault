# Generated by Django 4.1 on 2022-09-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='creatat',
        ),
        migrations.AddField(
            model_name='accessoir',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accessoir',
            name='original_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accessoir',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accessoir',
            name='selling_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accessoir',
            name='small_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
