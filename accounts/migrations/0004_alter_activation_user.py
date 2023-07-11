# Generated by Django 4.1.2 on 2023-07-11 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_alter_activation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accounts_activation', to=settings.AUTH_USER_MODEL),
        ),
    ]