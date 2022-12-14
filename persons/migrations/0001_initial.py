# Generated by Django 4.1.3 on 2022-11-16 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Имя')),
                ('surname', models.CharField(max_length=75, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=75, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Имя')),
                ('surname', models.CharField(max_length=75, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=75, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reference_info.branchofmedicine', verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
            },
        ),
    ]
