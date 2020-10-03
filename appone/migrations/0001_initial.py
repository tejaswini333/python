# Generated by Django 2.2.7 on 2020-08-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='user_name')),
                ('age', models.IntegerField(verbose_name='user_age')),
                ('salary', models.FloatField(verbose_name='user_salary')),
                ('address', models.CharField(max_length=20, verbose_name='user_address')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=20, unique=True, verbose_name='password')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='login', to='appone.Employee')),
            ],
        ),
    ]
