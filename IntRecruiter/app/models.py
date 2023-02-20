from django.conf import settings
from django.db import models


class UserExpasion(models.Model):
    OPTIONS = [
        ('EMP', 'employer'),
        ('WRK', 'worker'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.CharField(
        max_length=9,
        choices=OPTIONS,
        default='WRK',
        )

    def __str__(self):
        return f'Goal for user "{self.user}"'


class Employer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    count_worker = models.IntegerField()
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.user.username


class Worker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    info = models.TextField()
    contacts = models.CharField(max_length=100)
    work_exp = models.TextField()

    def __str__(self):
        return self.user.username


class Vacancy(models.Model):
    title = models.CharField(max_length=150)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    info = models.TextField()
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title
