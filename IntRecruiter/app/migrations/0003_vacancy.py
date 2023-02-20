# Generated by Django 4.1.3 on 2023-02-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_employer_user_worker_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('info', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
            ],
        ),
    ]