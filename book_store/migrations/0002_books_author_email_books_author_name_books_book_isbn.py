# Generated by Django 4.2.4 on 2023-08-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="author_email",
            field=models.EmailField(default="Unknown@o2.pl", max_length=255),
        ),
        migrations.AddField(
            model_name="books",
            name="author_name",
            field=models.CharField(default="Unknown", max_length=255),
        ),
        migrations.AddField(
            model_name="books",
            name="book_isbn",
            field=models.CharField(default="0000000000000", max_length=255),
        ),
    ]
