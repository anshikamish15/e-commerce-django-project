# Generated by Django 2.1.7 on 2021-02-06 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pro_img', models.ImageField(blank=True, upload_to='product_image')),
                ('qty', models.IntegerField()),
                ('dated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.UserProfile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Category')),
            ],
        ),
    ]
