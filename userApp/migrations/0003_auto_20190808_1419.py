# Generated by Django 2.2.3 on 2019-08-08 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20190808_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_number', models.CharField(default='0000000', max_length=50)),
                ('question', models.CharField(default='0000000', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('input', models.CharField(max_length=1000)),
                ('output', models.CharField(max_length=100)),
                ('que', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='0000000', max_length=250)),
                ('password', models.CharField(default='0000000', max_length=250)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='submissions',
            name='que',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Submissions',
        ),
        migrations.DeleteModel(
            name='UserProfiles',
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.UserProfile'),
        ),
    ]
