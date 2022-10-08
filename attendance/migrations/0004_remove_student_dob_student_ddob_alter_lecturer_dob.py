# Generated by Django 4.1.1 on 2022-10-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attendance_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='DOB',
        ),
        migrations.AddField(
            model_name='student',
            name='DDOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]