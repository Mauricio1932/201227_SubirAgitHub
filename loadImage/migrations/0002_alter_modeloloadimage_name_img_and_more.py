# Generated by Django 4.0.1 on 2022-02-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadImage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloloadimage',
            name='name_img',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='modeloloadimage',
            name='url_img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
