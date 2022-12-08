# Generated by Django 4.0 on 2022-12-01 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('actuvado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40)),
                ('resumen', models.CharField(max_length=70)),
                ('texto', models.TextField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to='post')),
                ('publicado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.categoria')),
            ],
            options={
                'verbose_name_plural': 'Posteos',
            },
        ),
    ]