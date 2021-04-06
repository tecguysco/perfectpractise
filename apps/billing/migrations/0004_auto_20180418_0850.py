# Generated by Django 2.0 on 2018-04-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_stripeinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billinginfo',
            name='has_paid',
        ),
        migrations.RemoveField(
            model_name='billinginfo',
            name='stripeToken',
        ),
        migrations.AddField(
            model_name='billinginfo',
            name='customer_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='billinginfo',
            name='subscription_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='stripeinfo',
            name='plan_id',
            field=models.CharField(max_length=256),
        ),
    ]