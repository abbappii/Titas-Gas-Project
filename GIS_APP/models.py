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

    # start 
    customer_id_20 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_20 = models.CharField(max_length=100, blank=True, null=True)
    status_20 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_20 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_20 = models.FloatField(blank=True, null=True)

    customer_id_21 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_21 = models.CharField(max_length=100, blank=True, null=True)
    status_21 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_21 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_21 = models.FloatField(blank=True, null=True)


    customer_id_22 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_22 = models.CharField(max_length=100, blank=True, null=True)
    status_22 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_22 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_22 = models.FloatField(blank=True, null=True)

    customer_id_23 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_23 = models.CharField(max_length=100, blank=True, null=True)
    status_23 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_23 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_23 = models.FloatField(blank=True, null=True)
    
    customer_id_24 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_24 = models.CharField(max_length=100, blank=True, null=True)
    status_24 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_24 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_24 = models.FloatField(blank=True, null=True)
    
    customer_id_25 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_25 = models.CharField(max_length=100, blank=True, null=True)
    status_25 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_25 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_25 = models.FloatField(blank=True, null=True)

    customer_id_26 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_26 = models.CharField(max_length=100, blank=True, null=True)
    status_26 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_26 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_26 = models.FloatField(blank=True, null=True)

    customer_id_27 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_27 = models.CharField(max_length=100, blank=True, null=True)
    status_27 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_27 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_27 = models.FloatField(blank=True, null=True)

    customer_id_28 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_28 = models.CharField(max_length=100, blank=True, null=True)
    status_28 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_28 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_28 = models.FloatField(blank=True, null=True)

    customer_id_29 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_29 = models.CharField(max_length=100, blank=True, null=True)
    status_29 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_29 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_29 = models.FloatField(blank=True, null=True)

    customer_id_30 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_30 = models.CharField(max_length=100, blank=True, null=True)
    status_30 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_30 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_30 = models.FloatField(blank=True, null=True)

    customer_id_31 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_31 = models.CharField(max_length=100, blank=True, null=True)
    status_31 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_31 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_31 = models.FloatField(blank=True, null=True)

    customer_id_32 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_32 = models.CharField(max_length=100, blank=True, null=True)
    status_32 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_32 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_32 = models.FloatField(blank=True, null=True)

    customer_id_33 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_33 = models.CharField(max_length=100, blank=True, null=True)
    status_33 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_33 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_33 = models.FloatField(blank=True, null=True)

    customer_id_34 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_34 = models.CharField(max_length=100, blank=True, null=True)
    status_34 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_34 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_34 = models.FloatField(blank=True, null=True)

    customer_id_35 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_35 = models.CharField(max_length=100, blank=True, null=True)
    status_35 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_35 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_35 = models.FloatField(blank=True, null=True)

    customer_id_36 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_36 = models.CharField(max_length=100, blank=True, null=True)
    status_36 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_36 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_36 = models.FloatField(blank=True, null=True)

    customer_id_37 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_37 = models.CharField(max_length=100, blank=True, null=True)
    status_37 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_37 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_37 = models.FloatField(blank=True, null=True)

    customer_id_38 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_38 = models.CharField(max_length=100, blank=True, null=True)
    status_38 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_38 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_38 = models.FloatField(blank=True, null=True)

    customer_id_39 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_39 = models.CharField(max_length=100, blank=True, null=True)
    status_39 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_39 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_39 = models.FloatField(blank=True, null=True)

    customer_id_40 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_40 = models.CharField(max_length=100, blank=True, null=True)
    status_40 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_40 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_40 = models.FloatField(blank=True, null=True)

    customer_id_41 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_41 = models.CharField(max_length=100, blank=True, null=True)
    status_41 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_41 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_41 = models.FloatField(blank=True, null=True)

    customer_id_42 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_42 = models.CharField(max_length=100, blank=True, null=True)
    status_42 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_42 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_42 = models.FloatField(blank=True, null=True)

    customer_id_43 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_43 = models.CharField(max_length=100, blank=True, null=True)
    status_43 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_43 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_43 = models.FloatField(blank=True, null=True)

    customer_id_44 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_44 = models.CharField(max_length=100, blank=True, null=True)
    status_44 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_44 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_44 = models.FloatField(blank=True, null=True)

    customer_id_45 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_45 = models.CharField(max_length=100, blank=True, null=True)
    status_45 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_45 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_45 = models.FloatField(blank=True, null=True)

    customer_id_46 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_46 = models.CharField(max_length=100, blank=True, null=True)
    status_46 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_46 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_46 = models.FloatField(blank=True, null=True)

    customer_id_47 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_47 = models.CharField(max_length=100, blank=True, null=True)
    status_47 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_47 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_47 = models.FloatField(blank=True, null=True)

    customer_id_48 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_48 = models.CharField(max_length=100, blank=True, null=True)
    status_48 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_48 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_48 = models.FloatField(blank=True, null=True)

    customer_id_49 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_49 = models.CharField(max_length=100, blank=True, null=True)
    status_49 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_49 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_49 = models.FloatField(blank=True, null=True)

    customer_id_50 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_50 = models.CharField(max_length=100, blank=True, null=True)
    status_50 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_50 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_50 = models.FloatField(blank=True, null=True)

    customer_id_51 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_51 = models.CharField(max_length=100, blank=True, null=True)
    status_51 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_51 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_51 = models.FloatField(blank=True, null=True)

    customer_id_52 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_52 = models.CharField(max_length=100, blank=True, null=True)
    status_52 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_52 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_52 = models.FloatField(blank=True, null=True)

    customer_id_53 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_53 = models.CharField(max_length=100, blank=True, null=True)
    status_53 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_53 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_53 = models.FloatField(blank=True, null=True)

    customer_id_54 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_54 = models.CharField(max_length=100, blank=True, null=True)
    status_54 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_54 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_54 = models.FloatField(blank=True, null=True)

    customer_id_55 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_55 = models.CharField(max_length=100, blank=True, null=True)
    status_55 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_55 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_55 = models.FloatField(blank=True, null=True)

    customer_id_56 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_56 = models.CharField(max_length=100, blank=True, null=True)
    status_56 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_56 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_56 = models.FloatField(blank=True, null=True)

    customer_id_57 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_57 = models.CharField(max_length=100, blank=True, null=True)
    status_57 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_57 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_57 = models.FloatField(blank=True, null=True)

    customer_id_58 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_58 = models.CharField(max_length=100, blank=True, null=True)
    status_58 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_58 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_58 = models.FloatField(blank=True, null=True)

    customer_id_59 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_59 = models.CharField(max_length=100, blank=True, null=True)
    status_59 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_59 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_59 = models.FloatField(blank=True, null=True)

    customer_id_60 = models.CharField(max_length=50, blank=True, null=True)
    customer_name_60 = models.CharField(max_length=100, blank=True, null=True)
    status_60 = models.CharField(max_length=50, blank=True, null=True)
    burner_type_60 = models.CharField(max_length=50, blank=True, null=True)
    burner_no_field_60 = models.FloatField(blank=True, null=True)

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