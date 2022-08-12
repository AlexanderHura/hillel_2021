# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    fio        = models.CharField('ФИО', max_length=255, default='')
    gender     = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='2000-09-12')
    phone = models.CharField('Телефон', max_length=255, default='')

    
