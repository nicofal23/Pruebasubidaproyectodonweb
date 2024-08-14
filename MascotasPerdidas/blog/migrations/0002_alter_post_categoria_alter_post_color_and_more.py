# Generated by Django 5.0.7 on 2024-08-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='zona',
            field=models.CharField(max_length=50),
        ),
    ]
