# Generated by Django 4.1.1 on 2022-10-01 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_alter_collegeday_theclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='attendance.student'),
        ),
    ]
