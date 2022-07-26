# Generated by Django 3.2 on 2022-07-26 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0004_auto_20220726_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='discussion',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
