# Generated by Django 3.2.9 on 2021-12-21 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_auto_20211216_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_days', to='curriculum.standard')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_time_slots', to='curriculum.standard')),
            ],
        ),
        migrations.CreateModel(
            name='SlotSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_days', to='curriculum.workingdays')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_time', to='curriculum.timeslots')),
                ('slot_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_subject', to='curriculum.subject')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots', to='curriculum.standard')),
            ],
        ),
    ]
