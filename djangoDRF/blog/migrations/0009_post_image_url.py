# Generated by Django 4.2.5 on 2023-11-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(blank=True, default='https://images.pexels.com/photos/171945/pexels-photo-171945.jpeg?auto=compress&cs=tinysrgb&w=400', max_length=500, null=True),
        ),
    ]