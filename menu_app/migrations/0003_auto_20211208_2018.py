# Generated by Django 3.2.6 on 2021-12-08 17:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_alter_menuitem_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='priority',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_label',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='menu_app.menu'),
        ),
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together={('menu', 'title')},
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['url', 'menu'], name='menu_app_me_url_65cfe3_idx'),
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu'], name='menu_app_me_menu_id_a0f054_idx'),
        ),
    ]