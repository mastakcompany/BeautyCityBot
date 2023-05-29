import uuid

from django.db import models


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Clients(UUIDMixin, TimeStampedMixin):
    telegram_id = models.IntegerField(unique=True)
    username = models.CharField(
        max_length=64,
        null=True,
        blank=False,
        verbose_name='User Name'
    )
    first_name = models.CharField(
        max_length=256,
        null=True,
        blank=False,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Phone Number'
    )
    email = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='email'
    )
    is_admin = models.BooleanField(
        null=True,
        blank=True,
        default=False,
        verbose_name='Администратор'
    )

    def __str__(self):
        if self.username:
            return f'@{self.username}'
        else:
            return f'{self.telegram_id}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Salon(UUIDMixin, TimeStampedMixin):
    name = models.CharField(
        'Наименование салона', max_length=200, db_index=True,
    )
    address = models.TextField(
        'Адрес Салона', blank=True, null=True)
    time_open = models.TimeField("время открытия")
    time_close = models.TimeField("время закрытия")

    def __str__(self):
        return self.name


class Service(UUIDMixin, TimeStampedMixin):
    salon = models.ForeignKey(Salon, verbose_name='Салон', related_name='salon_service',
                              blank=True, on_delete=models.CASCADE)
    name = models.CharField('Имя услуги', max_length=200, )
    price = models.CharField('Стоимость услуги', max_length=10)

    def __str__(self):
        return f'Салон: {self.salon}. Услуга:{self.name}. Цена: {self.price}.'


class Master(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField('ФИО мастера', max_length=200)
    salon = models.ForeignKey(Salon, verbose_name='Салон где работает Мастер', related_name='salon', blank=True,
                              on_delete=models.CASCADE, db_index=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.full_name


class Schedule(UUIDMixin, TimeStampedMixin):
    TIMEVISIT_LIST = (
        (0, '09:00 – 10:00'),
        (1, '10:00 – 11:00'),
        (2, '11:00 – 12:00'),
        (3, '12:00 – 13:00'),
        (4, '13:00 – 14:00'),
        (5, '15:00 – 16:00'),
        (6, '16:00 – 17:00'),
        (7, '17:00 – 18:00'),
        (8, '18:00 – 19:00'),
    )
    date = models.DateField('Дата посещения', help_text='YYYY-MM-DD')
    time_visit = models.IntegerField(choices=TIMEVISIT_LIST, null=True)
    client = models.ForeignKey(Clients, verbose_name='Имя клиента', on_delete=models.CASCADE,
                               related_name='schedules_user')
    salon = models.ForeignKey(Salon, verbose_name='Салон', on_delete=models.CASCADE, related_name='schedule_salon')
    master = models.ForeignKey(Master, verbose_name='Мастер', on_delete=models.CASCADE, related_name='schedule_master')
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.CASCADE,
                                related_name='schedule_service')
