# Generated by Django 3.0.7 on 2020-07-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_image_tags'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='imageusertagbox',
            name='unique_imagetaguser',
        ),
        migrations.AddConstraint(
            model_name='imageusertagbox',
            constraint=models.UniqueConstraint(fields=('image', 'tag', 'user', 'box'), name='unique_imagetaguserbox'),
        ),
    ]
