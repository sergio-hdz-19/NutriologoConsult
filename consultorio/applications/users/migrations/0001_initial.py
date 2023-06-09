# Generated by Django 4.2.1 on 2023-05-19 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Usuario')),
                ('name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('ocupation', models.CharField(blank=True, choices=[('0', 'Administrador'), ('1', 'Asistente'), ('2', 'Paciente')], max_length=1)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=1)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('actividad_aerobica', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
