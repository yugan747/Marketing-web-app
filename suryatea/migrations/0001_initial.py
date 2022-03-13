# Generated by Django 4.0.2 on 2022-03-13 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('Route', models.CharField(blank=True, max_length=120, null=True)),
                ('District', models.CharField(blank=True, choices=[('1', 'Kathmandu'), ('2', 'Lalitpur'), ('3', 'Bhaktapur')], max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('Contact1', models.PositiveIntegerField(blank=True, null=True)),
                ('Contact2', models.PositiveIntegerField(blank=True, null=True)),
                ('Customer_type', models.CharField(choices=[('HT', 'Hotel'), ('Kr', 'Kirana'), ('HM', 'Home'), ('OT', 'Others')], max_length=200)),
                ('AveragePrice', models.PositiveIntegerField(default=400)),
                ('Note', models.TextField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, upload_to='media/pictures')),
                ('Images_Map', models.ImageField(blank=True, upload_to='media/pictures')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(null=True)),
                ('Price', models.PositiveIntegerField(default=400)),
                ('Ordered_date', models.DateTimeField(auto_now_add=True)),
                ('District', models.CharField(blank=True, choices=[('1', 'Kathmandu'), ('2', 'Lalitpur'), ('3', 'Bhaktapur')], max_length=200)),
                ('ToVisit_date', models.DateField(null=True)),
                ('Visited', models.BooleanField(default=False)),
                ('rating', models.CharField(choices=[('3', 'Good'), ('2', 'Average'), ('1', 'Poor'), ('0', 'cash')], max_length=120)),
                ('Product', models.CharField(blank=True, max_length=200)),
                ('Hold', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suryatea.customer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='money_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.PositiveIntegerField(null=True)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suryatea.order')),
            ],
        ),
    ]
