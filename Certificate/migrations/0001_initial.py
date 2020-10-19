# Generated by Django 3.0.3 on 2020-10-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('alternate_contact_no', models.CharField(max_length=15, null=True)),
                ('course', models.CharField(max_length=150)),
                ('address', models.TextField()),
            ],
        ),
    ]