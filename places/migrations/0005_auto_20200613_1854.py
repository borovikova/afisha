# Generated by Django 3.0.7 on 2020-06-13 18:54

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_remove_place_detailsurl'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='порядок отображения картинки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='полное описание'),
        ),
    ]