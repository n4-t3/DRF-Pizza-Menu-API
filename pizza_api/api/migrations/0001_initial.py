# Generated by Django 4.1.1 on 2022-09-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('topping_1', models.IntegerField(choices=[(1, 'Pepperoni'), (2, 'Mushroom'), (3, 'Extra cheese'), (3, 'Sausage'), (4, 'Onion'), (5, 'Black olives'), (6, 'Green pepper'), (7, 'Fresh garlic'), (8, 'Tomato'), (9, 'Fresh basil')], default=1)),
                ('topping_2', models.IntegerField(choices=[(1, 'Pepperoni'), (2, 'Mushroom'), (3, 'Extra cheese'), (3, 'Sausage'), (4, 'Onion'), (5, 'Black olives'), (6, 'Green pepper'), (7, 'Fresh garlic'), (8, 'Tomato'), (9, 'Fresh basil')], default=3)),
                ('topping_3', models.IntegerField(choices=[(1, 'Pepperoni'), (2, 'Mushroom'), (3, 'Extra cheese'), (3, 'Sausage'), (4, 'Onion'), (5, 'Black olives'), (6, 'Green pepper'), (7, 'Fresh garlic'), (8, 'Tomato'), (9, 'Fresh basil')], default=6)),
                ('size', models.IntegerField(choices=[(1, 'Small'), (2, 'Medium'), (3, 'Large')], default=2)),
                ('average_rating', models.FloatField(default=0)),
                ('number_of_ratings', models.IntegerField(default=0)),
            ],
        ),
    ]
