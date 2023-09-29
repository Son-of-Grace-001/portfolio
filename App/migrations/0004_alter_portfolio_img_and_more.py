# Generated by Django 4.2.5 on 2023-09-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_portfolio_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(upload_to='portfolio_images/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_link_code',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_source_link',
            field=models.URLField(),
        ),
    ]
