# Generated by Django 5.1 on 2024-08-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_employee_department_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved by TL', 'Approved by TL'), ('Approved by Manager', 'Approved by Manager'), ('Rejected', 'Rejected')], default='Pending', max_length=30),
        ),
    ]
