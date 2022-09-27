# Generated by Django 4.0.3 on 2022-09-27 09:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.FloatField()),
                ('depth', models.FloatField(default=0)),
                ('len', models.FloatField(default=None)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32646)),
            ],
            options={
                'verbose_name_plural': 'Casing Model',
            },
        ),
        migrations.CreateModel(
            name='DRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32646)),
            ],
            options={
                'verbose_name_plural': 'DRS Model',
            },
        ),
        migrations.CreateModel(
            name='EndCapModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='FootPathShapeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='GasLineShapeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.FloatField()),
                ('depth', models.FloatField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('len', models.FloatField(default=None)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='PlotShapeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.CharField(blank=True, max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='ReducerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='RiserShapeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_1', models.CharField(blank=True, max_length=100, null=True)),
                ('status_1', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_typ', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_no_field', models.FloatField(blank=True, null=True)),
                ('customer_2', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_3', models.CharField(blank=True, max_length=100, null=True)),
                ('status_2', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_1', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_no1', models.FloatField(blank=True, null=True)),
                ('customer_4', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_5', models.CharField(blank=True, max_length=100, null=True)),
                ('status_3', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_2', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_1', models.FloatField(blank=True, null=True)),
                ('customer_6', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_7', models.CharField(blank=True, max_length=100, null=True)),
                ('status_4', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_3', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_2', models.FloatField(blank=True, null=True)),
                ('customer_8', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_9', models.CharField(blank=True, max_length=100, null=True)),
                ('status_5', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_4', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_3', models.FloatField(blank=True, null=True)),
                ('custome_10', models.CharField(blank=True, max_length=50, null=True)),
                ('custome_11', models.CharField(blank=True, max_length=100, null=True)),
                ('status_6', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_5', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_4', models.FloatField(blank=True, null=True)),
                ('custome_12', models.CharField(blank=True, max_length=50, null=True)),
                ('custome_13', models.CharField(blank=True, max_length=100, null=True)),
                ('status_7', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_6', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_5', models.FloatField(blank=True, null=True)),
                ('custome_14', models.CharField(blank=True, max_length=50, null=True)),
                ('custome_15', models.CharField(blank=True, max_length=100, null=True)),
                ('status_8', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_7', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_6', models.FloatField(blank=True, null=True)),
                ('custome_16', models.CharField(blank=True, max_length=50, null=True)),
                ('custome_17', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_8', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_7', models.FloatField(blank=True, null=True)),
                ('custome_18', models.CharField(blank=True, max_length=50, null=True)),
                ('custome_19', models.CharField(blank=True, max_length=100, null=True)),
                ('status_10', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_t_9', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_8', models.FloatField(blank=True, null=True)),
                ('burner_10', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_n_9', models.FloatField(blank=True, null=True)),
                ('burner_11', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_12', models.FloatField(blank=True, null=True)),
                ('burner_13', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_14', models.FloatField(blank=True, null=True)),
                ('burner_15', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_16', models.FloatField(blank=True, null=True)),
                ('burner_17', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_18', models.FloatField(blank=True, null=True)),
                ('burner_19', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_20', models.FloatField(blank=True, null=True)),
                ('burner_21', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_22', models.FloatField(blank=True, null=True)),
                ('burner_23', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_24', models.FloatField(blank=True, null=True)),
                ('burner_25', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_26', models.FloatField(blank=True, null=True)),
                ('burner_27', models.CharField(blank=True, max_length=50, null=True)),
                ('burner_28', models.FloatField(blank=True, null=True)),
                ('total_load', models.CharField(blank=True, max_length=50, null=True)),
                ('pressure_o', models.CharField(blank=True, max_length=50, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='RoadShapeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_no', models.CharField(blank=True, max_length=50, null=True)),
                ('shape_leng', models.FloatField(blank=True, null=True)),
                ('shape_area', models.FloatField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32646)),
            ],
        ),
        migrations.CreateModel(
            name='ValvePitShapeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.FloatField(default=None)),
                ('pressure', models.FloatField(blank=True, null=True)),
                ('valve_type', models.CharField(blank=True, max_length=50)),
                ('valvepit_s', models.CharField(blank=True, max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32646)),
            ],
        ),
    ]