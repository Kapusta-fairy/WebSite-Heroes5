# Generated by Django 4.0.4 on 2022-06-09 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=20, verbose_name='Фракция')),
            ],
            options={
                'verbose_name': 'фракция',
                'verbose_name_plural': 'Фракции',
                'ordering': ['-title'],
            },
        ),
        migrations.AlterModelOptions(
            name='downloadgame',
            options={'ordering': ['-title'], 'verbose_name': 'способ скачивание игры', 'verbose_name_plural': 'способы скачивания игры'},
        ),
        migrations.AlterModelOptions(
            name='maps',
            options={'ordering': ['title'], 'verbose_name': 'карта', 'verbose_name_plural': 'Карты'},
        ),
        migrations.AlterModelOptions(
            name='mods',
            options={'ordering': ['title'], 'verbose_name': 'мод', 'verbose_name_plural': 'Моды'},
        ),
        migrations.AlterModelOptions(
            name='online',
            options={'ordering': ['-title'], 'verbose_name': 'cпособ играть по сети', 'verbose_name_plural': 'Способы игры по сети'},
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('victory', models.BooleanField()),
                ('myself', models.CharField(max_length=20, verbose_name='Игрок')),
                ('opponent', models.CharField(max_length=20, verbose_name='Оппонент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('fraction_myself', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fraction_opponent', to='main.fraction', verbose_name='Фракция игрока')),
                ('fraction_opponent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.fraction', verbose_name='Фракция оппонента')),
            ],
            options={
                'verbose_name': 'Отчёт',
                'verbose_name_plural': 'Отчёты',
                'ordering': ['-created_at'],
            },
        ),
    ]