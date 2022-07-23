# Generated by Django 4.0 on 2022-07-20 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=255, verbose_name='Texto de Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.userprofile', verbose_name='Perfil del Usuario')),
            ],
        ),
    ]