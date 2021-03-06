# Generated by Django 3.2.3 on 2021-05-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.TextField(unique=True)),
                ('game_code', models.CharField(max_length=8)),
                ('p1_name', models.TextField(null=True)),
                ('p2_name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.TextField()),
                ('p_code', models.CharField(default='', max_length=8)),
                ('room_name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
