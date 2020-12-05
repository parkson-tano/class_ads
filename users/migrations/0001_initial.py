# Generated by Django 3.1.1 on 2020-10-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Choose not to say', 'choose not to  say')], max_length=20)),
                ('pass1', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]