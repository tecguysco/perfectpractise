# Generated by Django 2.0 on 2018-04-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_paid', models.BooleanField(default=False)),
                ('stripeToken', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
