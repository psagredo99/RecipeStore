# Generated by Django 3.2.8 on 2022-01-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(default='salt', null=True, to='main.Ingredient'),
        ),
    ]