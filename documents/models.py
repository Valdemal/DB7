from django.db import models

from persons.models import Patient, Doctor
from reference_info.models import Service, Diagnosis


class Referral(models.Model):
    patient = models.ForeignKey(
        Patient, models.DO_NOTHING, verbose_name='Пациент'
    )

    doctor = models.ForeignKey(
        Doctor, models.DO_NOTHING, verbose_name='Доктор'
    )

    service = models.ForeignKey(
        Service, models.DO_NOTHING, verbose_name='Услуга'
    )

    registration_time = models.DateTimeField(verbose_name='Время регистрации', auto_now_add=True)
    appointment_time = models.DateTimeField(verbose_name='Время приема')
    cabinet = models.CharField(max_length=100, verbose_name='Кабинет')

    class Result(models.TextChoices):
        PLANNED = 'Услуга запланирована'
        NO_PATIENT = 'Пациент не явился'
        PROVIDED = 'Услуга предоставлена'
        NOT_PROVIDED = 'Услуга не предоставлена'

    result = models.CharField(
        verbose_name='Результат', max_length=50,
        choices=Result.choices,
        default=Result.PLANNED
    )

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направление'


class Conclusion(models.Model):
    patient = models.ForeignKey(
        Patient, models.DO_NOTHING, verbose_name='Пациент'
    )

    doctor = models.ForeignKey(
        Doctor, models.DO_NOTHING, verbose_name='Доктор'
    )

    diagnosis = models.ForeignKey(
        Diagnosis, models.DO_NOTHING, verbose_name='Услуга'
    )

    registration_time = models.DateTimeField(verbose_name='Время регистрации', auto_now_add=True)

    class Status(models.TextChoices):
        HILLED = 'Вылечено'
        LETAL = 'Летальный исход'
        CRONIC = 'Хронический характер'
        IN_HILLING_PROCESS = 'В процессе лечения'

    status = models.CharField(
        max_length=50, verbose_name='Статус',
        choices=Status.choices, default=Status.IN_HILLING_PROCESS
    )

    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Заключение'
        verbose_name_plural = 'Заключения'
