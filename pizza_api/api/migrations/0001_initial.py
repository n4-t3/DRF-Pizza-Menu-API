# Generated by Django 4.1.1 on 2022-10-13 08:18

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
                ('topping_1', models.IntegerField(choices=[(1, 'Pepperoni'), (2, 'Mushroom'), (3, 'Extra cheese'), (4, 'Sausage'), (5, 'Onion'), (6, 'Black olives'), (7, 'Green pepper'), (8, 'Fresh garlic'), (9, 'Tomato'), (10, 'Fresh basil')], default=1)),
                ('topping_2', models.IntegerField(choices=[(1, 'Pepperoni'), (2, 'Mushroom'), (3, 'Extra cheese'), (4, 'Sausage'), (5, 'Onion'), (6, 'Black olives'), (7, 'Green pepper'), (8, 'Fresh garlic'), (9, 'Tomato'), (10, 'Fresh basil')], default=3)),
                ('topping_3', models.IntegerField(choices=[(1, 'Pepperoni'), (2, 'Mushroom'), (3, 'Extra cheese'), (4, 'Sausage'), (5, 'Onion'), (6, 'Black olives'), (7, 'Green pepper'), (8, 'Fresh garlic'), (9, 'Tomato'), (10, 'Fresh basil')], default=6)),
                ('size', models.IntegerField(choices=[(1, 'Small'), (2, 'Medium'), (3, 'Large')], default=2)),
                ('picture', models.ImageField(default='pizza-images/ivan-torres-MQUqbmszGGM-unsplash.jpg', upload_to='pizza-images')),
                ('average_rating', models.FloatField(default=0)),
                ('number_of_ratings', models.IntegerField(default=0)),
            ],
        ),
    ]
