from ftplib import MAXLINE
from tabnanny import verbose
from django.contrib.gis.db import models


# Create your models here.


class PlotShapeModel(models.Model):
    plot = models.CharField(max_length=100, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32646)

    def __unicode__(self):
        return self.plot


class RoadShapeModel(models.Model):
    road_no = models.CharField(max_length=50, blank=True, null=True)
    # rd_w_ft = models.FloatField(blank=True, null=True)
    # length = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=32646)


class GasLineShapeModel(models.Model):
    dia = models.FloatField()
    depth = models.FloatField(default=0)
    pressure = models.IntegerField(default=0)
    len = models.FloatField(default=None)
    geom = models.MultiLineStringField(srid=32646)


# class RiserShapeModel(models.Model):
#     dia = models.FloatField()
#     pressure = models.FloatField(default=0)
#     cus_id = models.CharField(max_length=50, blank=True, null=True)
#     no_of_burn = models.FloatField(default=0, null=True)
#     load_conne = models.FloatField(default=0, null=True)
#     pressure_o = models.FloatField(default=0, null=True)
#     mon_load = models.FloatField(default=None, null=True)
#     geom = models.MultiPointField(srid=32646)

class RiserShapeModel(models.Model):
    customerid = models.CharField(max_length=50, blank=True, null=True)
    customer_1 = models.CharField(max_length=100, blank=True, null=True)
    status_1 = models.CharField(max_length=50, blank=True, null=True)
    burner_typ = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field = models.FloatField(blank=True, null=True)
    customer_2 = models.CharField(max_length=50, blank=True, null=True)
    customer_3 = models.CharField(max_length=100, blank=True, null=True)
    status_2 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_1 = models.CharField(max_length=50, blank=True, null=True)
    burner_no1 = models.FloatField(blank=True, null=True)
    customer_4 = models.CharField(max_length=50, blank=True, null=True)
    customer_5 = models.CharField(max_length=100, blank=True, null=True)
    status_3 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_2 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_1 = models.FloatField(blank=True, null=True)
    customer_6 = models.CharField(max_length=50, blank=True, null=True)
    customer_7 = models.CharField(max_length=100, blank=True, null=True)
    status_4 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_3 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_2 = models.FloatField(blank=True, null=True)
    customer_8 = models.CharField(max_length=50, blank=True, null=True)
    customer_9 = models.CharField(max_length=100, blank=True, null=True)
    status_5 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_4 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_3 = models.FloatField(blank=True, null=True)
    custome_10 = models.CharField(max_length=50, blank=True, null=True)
    custome_11 = models.CharField(max_length=100, blank=True, null=True)
    status_6 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_5 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_4 = models.FloatField(blank=True, null=True)
    custome_12 = models.CharField(max_length=50, blank=True, null=True)
    custome_13 = models.CharField(max_length=100, blank=True, null=True)
    status_7 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_6 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_5 = models.FloatField(blank=True, null=True)
    custome_14 = models.CharField(max_length=50, blank=True, null=True)
    custome_15 = models.CharField(max_length=100, blank=True, null=True)
    status_8 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_7 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_6 = models.FloatField(blank=True, null=True)
    custome_16 = models.CharField(max_length=50, blank=True, null=True)
    custome_17 = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    burner_t_8 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_7 = models.FloatField(blank=True, null=True)
    custome_18 = models.CharField(max_length=50, blank=True, null=True)
    custome_19 = models.CharField(max_length=100, blank=True, null=True)
    status_10 = models.CharField(max_length=50, blank=True, null=True)
    burner_t_9 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_8 = models.FloatField(blank=True, null=True)
    burner_10 = models.CharField(max_length=50, blank=True, null=True)
    burner_n_9 = models.FloatField(blank=True, null=True)
    burner_11 = models.CharField(max_length=50, blank=True, null=True)
    burner_12 = models.FloatField(blank=True, null=True)
    burner_13 = models.CharField(max_length=50, blank=True, null=True)
    burner_14 = models.FloatField(blank=True, null=True)
    burner_15 = models.CharField(max_length=50, blank=True, null=True)
    burner_16 = models.FloatField(blank=True, null=True)
    burner_17 = models.CharField(max_length=50, blank=True, null=True)
    burner_18 = models.FloatField(blank=True, null=True)
    burner_19 = models.CharField(max_length=50, blank=True, null=True)
    burner_20 = models.FloatField(blank=True, null=True)
    burner_21 = models.CharField(max_length=50, blank=True, null=True)
    burner_22 = models.FloatField(blank=True, null=True)
    burner_23 = models.CharField(max_length=50, blank=True, null=True)
    burner_24 = models.FloatField(blank=True, null=True)
    burner_25 = models.CharField(max_length=50, blank=True, null=True)
    burner_26 = models.FloatField(blank=True, null=True)
    burner_27 = models.CharField(max_length=50, blank=True, null=True)
    burner_28 = models.FloatField(blank=True, null=True)
    total_load = models.CharField(max_length=50, blank=True, null=True)
    pressure_o = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPointField(srid=32646)


class ValvePitShapeModel(models.Model):
    depth = models.FloatField(default=None)
    pressure = models.FloatField(blank=True, null=True)
    valve_type = models.CharField(max_length=50, blank=True)
    valvepit_s = models.CharField(max_length=50, blank=True)
    geom = models.MultiPointField(srid=32646)


class FootPathShapeModel(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=32646)


class EndCapModel(models.Model):
    geom = models.MultiPointField(srid=32646)


class ReducerModel(models.Model):
    geom = models.MultiPointField(srid=32646)


class CasingModel(models.Model):
    dia = models.FloatField()
    depth = models.FloatField(default=0)
    len = models.FloatField(default=None)
    geom = models.MultiPointField(srid=32646)

    def __str__(self):
        return f"Casing Model"

    class Meta:
        verbose_name_plural = "Casing Model"


class DRS(models.Model):
    name = models.CharField(max_length=255)
    geom = models.MultiPointField(srid=32646)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ="DRS Model"