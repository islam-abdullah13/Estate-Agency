# Generated by Django 3.1.7 on 2021-03-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='image',
            field=models.ImageField(default='', upload_to='estates/'),
            preserve_default=False,
        ),
    ]