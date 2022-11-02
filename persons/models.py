from django.db import models

from reference_info.models import BranchOfMedicine


class Doctor(models.Model):
    specialization = models.ForeignKey(
        BranchOfMedicine, models.DO_NOTHING,
        verbose_name='Специализация',
        db_column='specialization'
    )

    name = models.CharField(max_length=75, verbose_name='Имя')
    surname = models.CharField(max_length=75, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=75, blank=True, null=True, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Email')

    class Meta:
        managed = False
        db_table = 'doctor'
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'


class Patient(models.Model):
    name = models.CharField(max_length=75, verbose_name='Имя')
    surname = models.CharField(max_length=75, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=75, blank=True, null=True, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Email')

    class Meta:
        managed = False
        db_table = 'patient'
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
