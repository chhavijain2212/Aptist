# Generated by Django 2.0.2 on 2018-04-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apti', '0002_stream_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='op1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='op2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='op3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='op4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='questions',
            name='ques',
            field=models.CharField(max_length=5000),
        ),
    ]
