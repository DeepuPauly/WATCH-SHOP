# Generated by Django 3.0 on 2024-01-17 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_prestige_watch_marketplace_app', '0003_auto_20240117_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_category',
            old_name='Cat_Desc',
            new_name='Car_Desc',
        ),
        migrations.AlterField(
            model_name='tbl_customer',
            name='USERNAME',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_prestige_watch_marketplace_app.tbl_login'),
        ),
        migrations.AlterField(
            model_name='tbl_staff',
            name='USERNAME',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_prestige_watch_marketplace_app.tbl_login'),
        ),
    ]
