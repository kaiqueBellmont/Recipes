# Generated by Django 4.1.2 on 2022-11-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_remove_recipe_conclusion_datetime_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="conclusion_date",
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cover",
            field=models.ImageField(
                blank=True, default="", upload_to="recipes/covers/%Y/%m/%d/"
            ),
        ),
    ]
