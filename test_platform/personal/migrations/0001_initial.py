# Generated by Django 2.2 on 2019-04-09 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Project',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('name', models.CharField(max_length=40)),
				('describe', models.TextField(default='')),
				('status', models.BooleanField(default=1)),
				('create_time', models.DateTimeField(auto_now_add=True)),
			],
		),
		migrations.CreateModel(
			name='Module',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('name', models.CharField(max_length=50)),
				('describe', models.TextField(default='')),
				('create_time', models.DateTimeField(auto_now_add=True)),
				('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Project')),
			],
		),
	]
