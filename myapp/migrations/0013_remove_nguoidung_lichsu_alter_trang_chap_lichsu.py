# Generated by Django 4.2.7 on 2024-10-31 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_thongbao_theloai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nguoidung',
            name='lichsu',
        ),
        migrations.AlterField(
            model_name='trang',
            name='chap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trang', to='myapp.chap'),
        ),
        migrations.CreateModel(
            name='Lichsu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idchap', models.IntegerField()),
                ('idtruyen', models.IntegerField()),
                ('thoigiandoc', models.DateTimeField(auto_now_add=True)),
                ('nguoidoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lichsu', to='myapp.nguoidung')),
            ],
        ),
    ]
