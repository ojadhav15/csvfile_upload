# Generated by Django 5.0.1 on 2024-01-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_fileuploadmodel_file_fileuploadmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuploadmodel',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
