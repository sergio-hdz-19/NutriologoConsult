# Generated by Django 4.2.1 on 2023-05-19 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_is_active'),
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedleads', to='users.patient'),
        ),
    ]