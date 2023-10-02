from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'Администратор'),
    (VIPClient, 'VIP Клиент'),
    (CLIENT, 'Клиент')
)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'М'),
    (FEMALE, 'Ж')
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE,
                                    verbose_name="Выберите тип пользователя")
    phone_number = models.CharField('ваш сотовый:', max_length=13)
    age = models.PositiveIntegerField('Укажите возраст?', default=15)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Ваш пол')
