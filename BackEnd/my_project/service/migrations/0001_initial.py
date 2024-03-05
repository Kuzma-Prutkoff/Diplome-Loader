# Generated by Django 4.2.10 on 2024-03-01 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breakage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Узел отказа',
                'verbose_name_plural': 'Узлы отказа',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=32, unique=True, verbose_name='Зав. № машины')),
                ('engine_id', models.CharField(max_length=32, unique=True, verbose_name='Зав. № двигателя')),
                ('transmission_id', models.CharField(max_length=32, unique=True, verbose_name='Зав. № трансмиссии')),
                ('driving_axle_id', models.CharField(max_length=32, unique=True, verbose_name='Зав. № ведущего моста')),
                ('steering_axle_id', models.CharField(max_length=32, unique=True, verbose_name='Зав. № управляемого моста')),
                ('delivery_contract', models.CharField(max_length=256, verbose_name='Договор поставки №, дата')),
                ('discharge_date', models.DateField(verbose_name='Дата отгрузки с завода')),
                ('receiver', models.CharField(max_length=256, verbose_name='Грузополучатель')),
                ('delivery_address', models.CharField(max_length=256, verbose_name='Адрес поставки')),
                ('vehicle_configuration', models.CharField(max_length=512, verbose_name='Комплектация')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ['-discharge_date'],
            },
        ),
        migrations.CreateModel(
            name='DrivingAxle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель ведущего моста',
                'verbose_name_plural': 'Модели ведущего моста',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель двигателя',
                'verbose_name_plural': 'Модели двигателя',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид технического обслуживания',
                'verbose_name_plural': 'Виды технического обслуживания',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ восстановления',
                'verbose_name_plural': 'Способы восстановления',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('login_nickname', models.CharField(max_length=64, unique=True, verbose_name='Логин для входа')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SteeringAxle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель управляемого моста',
                'verbose_name_plural': 'Модели управляемого моста',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель трансмиссии',
                'verbose_name_plural': 'Модели трансмиссии',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель погрузчика',
                'verbose_name_plural': 'Модели погрузчика',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField(verbose_name='Дата проведения ТО')),
                ('running_time', models.IntegerField(verbose_name='Наработка м/час')),
                ('order_id', models.CharField(max_length=32, unique=True, verbose_name='Номер заказ-наряда')),
                ('order_date', models.DateField(verbose_name='Дата заказ-наряда')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.car', verbose_name='Машина')),
                ('maintenance_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.maintenancetype', verbose_name='Вид ТО')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.servicecompany', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Техническое обслуживание',
                'ordering': ['-maintenance_date'],
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakage_date', models.DateField(verbose_name='Дата отказа')),
                ('breakage_description', models.TextField(verbose_name='Описание отказа')),
                ('running_time', models.IntegerField(verbose_name='Наработка м/час')),
                ('spares', models.CharField(blank=True, max_length=256, verbose_name='Используемые запасные части')),
                ('repair_date', models.DateField(verbose_name='Дата восстановления')),
                ('down_time', models.IntegerField(verbose_name='Время простоя')),
                ('breakage_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.breakage', verbose_name='Узел отказа')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.car', verbose_name='Машина')),
                ('repairing_way', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.repair', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.servicecompany', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
                'ordering': ['-breakage_date'],
            },
        ),
        migrations.AddField(
            model_name='car',
            name='driving_axle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.drivingaxle', verbose_name='Модель ведущего моста'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.engine', verbose_name='Модель двигателя'),
        ),
        migrations.AddField(
            model_name='car',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.servicecompany', verbose_name='Сервисная компания'),
        ),
        migrations.AddField(
            model_name='car',
            name='steering_axle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.steeringaxle', verbose_name='Модель управляемого моста'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.transmission', verbose_name='Модель трансмиссии'),
        ),
        migrations.AddField(
            model_name='car',
            name='vehicle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.vehicle', verbose_name='Модель техники'),
        ),
    ]
