# Generated by Django 4.1.7 on 2023-04-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_ngo"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="pdf_file",
            field=models.FileField(blank=True, null=True, upload_to="pdf_files"),
        ),
    ]
