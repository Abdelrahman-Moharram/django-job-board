# Generated by Django 3.2.4 on 2021-06-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20210618_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Remotly', 'Remotly'), ('Full Time', 'Full Time'), ('Internship', 'Internship')], max_length=50),
        ),
    ]