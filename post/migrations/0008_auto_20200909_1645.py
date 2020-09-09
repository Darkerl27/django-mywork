# Generated by Django 3.0.3 on 2020-09-09 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('post', '0007_auto_20200909_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customuser', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customuser', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_post', to='users.customuser'),
        ),
    ]
