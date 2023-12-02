# Generated by Django 3.2.19 on 2023-06-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_form_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
    ]