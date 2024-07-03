# Generated by Django 5.0.6 on 2024-07-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(default='Description not provided')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(default='Description not provided')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(default='Description not provided')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about',
        ),
        migrations.RemoveField(
            model_name='about',
            name='nombre',
        ),
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default='Temporary default description', max_length=100),
            preserve_default=False,
        ),
    ]
