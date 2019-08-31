# Generated by Django 2.2.3 on 2019-08-31 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0007_auto_20190825_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='choice',
            field=models.CharField(default='cpp', max_length=5),
        ),
        migrations.AlterField(
            model_name='multipleques',
            name='que',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.Question'),
        ),
    ]
