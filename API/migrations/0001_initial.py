# Generated by Django 2.2 on 2019-04-02 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(max_length=512)),
                ('points', models.IntegerField(default=0)),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
