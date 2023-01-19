# Generated by Django 4.0.6 on 2023-01-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_details', '0003_alter_trainer_feedback_train_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer_feedback',
            name='train_id',
        ),
        migrations.AddField(
            model_name='trainer_feedback',
            name='train_data',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='trainer_data',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]