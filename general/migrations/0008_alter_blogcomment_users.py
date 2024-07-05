# Generated by Django 5.0.6 on 2024-07-05 17:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_blogcomment_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='users',
            field=models.ManyToManyField(null=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
