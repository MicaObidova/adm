# Generated by Django 4.0.4 on 2022-10-19 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ads',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.region'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.BigIntegerField(null=True),
        ),
    ]