# Generated by Django 2.2 on 2019-06-17 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artigo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artigos', to='categoria.Categoria'),
        ),
    ]