# Generated by Django 4.2.2 on 2023-06-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('Nebulosa', 'Nebulosa'), ('Estrela', 'Estrela'), ('Galáxia', 'Galáxia'), ('Planeta', 'Planeta')], default='', max_length=100),
        ),
    ]
