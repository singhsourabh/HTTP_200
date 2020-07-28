# Generated by Django 3.0.8 on 2020-07-27 13:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.URLField(max_length=100)),
                ('message', models.TextField()),
                ('message_sent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(blank=True, choices=[('BTech', 'BTech'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('MTech', 'MTech'), ('Humanities', 'Humanities'), ('English', 'English'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Maths', 'Maths'), ('Administration', 'Administration'), ('Maintenance', 'Maintenance'), ('OTHER', 'Others')], default='AllCourses', max_length=15, null=True)),
                ('branch', models.CharField(blank=True, choices=[('AllBranches', 'None'), ('CSE', 'Computer Science and Engineering'), ('IT', 'Information Technology'), ('EE', 'Electrical Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('CE', 'Civil Engineering'), ('IC', 'Instrumentation and Control Engineering'), ('ME', 'Mechanical Engineering'), ('MT', 'Manufacturing Technology')], default='AllBranches', max_length=15, null=True)),
                ('year', models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('section', models.CharField(blank=True, choices=[('AllSections', 'None'), ('CSE1', 'CSE1'), ('CSE2', 'CSE2'), ('IT1', 'IT1'), ('IT2', 'IT2'), ('ECE1', 'ECE1'), ('ECE2', 'ECE2'), ('EE1', 'EE1'), ('EE2', 'EE2'), ('EEE1', 'EEE1'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('IC1', 'IC1'), ('IC2', 'IC2'), ('MT1', 'MT1'), ('MT2', 'MT2'), ('ME1', 'ME1'), ('ME2', 'ME2'), ('ME3', 'ME3')], default='AllSections', max_length=15, null=True)),
                ('univ_roll_no', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=10, null=True)),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('display_to_others', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('alternate_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('display_to_others', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
