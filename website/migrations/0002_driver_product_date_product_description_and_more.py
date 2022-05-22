# Generated by Django 4.0.1 on 2022-05-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=1000)),
                ('last', models.CharField(max_length=1000)),
                ('id_number', models.IntegerField(default=None)),
                ('type', models.CharField(max_length=1000)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='none', max_length=100000),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
