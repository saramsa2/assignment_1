# Generated by Django 4.1.1 on 2022-10-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_remove_student_dob_student_ddob_alter_lecturer_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='student',
            field=models.ManyToManyField(to='attendance.student', verbose_name='enrolled student'),
        ),
    ]
