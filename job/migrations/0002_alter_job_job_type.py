# Generated by Django 3.2.4 on 2021-06-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Remotly', 'Remotly'), ('Internship', 'Internship')], max_length=50),
        ),
    ]