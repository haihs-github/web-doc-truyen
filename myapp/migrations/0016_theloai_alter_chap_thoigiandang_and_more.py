# Generated by Django 4.2.7 on 2024-11-04 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_lichsu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theloai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theloai', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='chap',
            name='thoigiandang',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lichsu',
            name='thoigiandoc',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]