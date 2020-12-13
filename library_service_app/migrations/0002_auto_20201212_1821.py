# Generated by Django 2.2 on 2020-12-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_service_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
