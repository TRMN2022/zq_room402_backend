# Generated by Django 4.1 on 2022-11-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=16, verbose_name="姓名")),
                ("password", models.CharField(max_length=32, verbose_name="密码")),
                ("phone", models.CharField(max_length=11, verbose_name="手机号码")),
                ("group", models.CharField(max_length=16, verbose_name="组别")),
                ("job", models.CharField(max_length=16, verbose_name="职务")),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户",
                "db_table": "402_users",
            },
        ),
    ]
