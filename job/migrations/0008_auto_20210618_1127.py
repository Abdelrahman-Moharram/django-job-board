# Generated by Django 3.2.4 on 2021-06-18 11:27

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20210618_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('protifolio', models.URLField()),
                ('cv', models.FileField(upload_to=job.models.cv_upload)),
                ('coverLetter', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Remotly', 'Remotly'), ('Internship', 'Internship'), ('Full Time', 'Full Time')], max_length=50),
        ),
    ]