# Generated by Django 2.2 on 2019-04-07 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Answers',
        ),
        migrations.AlterField(
            model_name='task',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Exam'),
        ),
    ]
