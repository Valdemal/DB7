from django.db import models


class BranchOfMedicine(models.Model):
    name = models.CharField(unique=True, max_length=120, verbose_name='Название')

    class Meta:
        managed = False
        db_table = 'branch_of_medicine'
        verbose_name = 'Отрасль медицины'
        verbose_name_plural = 'Отрасли медицины'


class Diagnosis(models.Model):
    name = models.CharField(unique=True, max_length=120, verbose_name='Название')
    branch = models.ForeignKey(BranchOfMedicine, models.DO_NOTHING, verbose_name='Отрасль медицины')

    class Meta:
        managed = False
        db_table = 'diagnosis'
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'


class Service(models.Model):
    name = models.CharField(unique=True, max_length=120, verbose_name='Название')
    branch = models.ForeignKey(BranchOfMedicine, models.DO_NOTHING, verbose_name='Отрасль медицины')

    class Meta:
        managed = False
        db_table = 'service'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
