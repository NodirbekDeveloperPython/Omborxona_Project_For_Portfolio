# Generated by Django 4.1.3 on 2023-01-09 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiyapp', '0001_initial'),
        ('userapp', '0002_remove_sotuvchi_user_sotuvchi_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField(default=1)),
                ('jami', models.PositiveSmallIntegerField()),
                ('tolandi', models.PositiveSmallIntegerField()),
                ('nasya', models.PositiveSmallIntegerField(default=0)),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyapp.mahsulot')),
                ('mijoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asosiyapp.mijoz')),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
    ]
