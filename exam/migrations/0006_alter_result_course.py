# Generated by Django 4.0.3 on 2022-06-02 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.course'),
        ),
    ]
