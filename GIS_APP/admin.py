from django.contrib import admin
from GIS_APP import models as gis_model
from leaflet.admin import LeafletGeoAdmin 

# Register your models here.

# @admin.register(gis_model.PlotShapeModel)
# class PlotShapeModel(admin.ModelAdmin):
#     list_display = ('id', 'geom', 'plot')

admin.site.register(gis_model.PlotShapeModel,LeafletGeoAdmin) 


@admin.register(gis_model.RoadShapeModel)
class RoadShapeModel(admin.ModelAdmin):
    list_display = ('id', 'road_no', 'geom')

@admin.register(gis_model.GasLineShapeModel)
class GasLineShapeModel(admin.ModelAdmin):
    list_display = ('id', 'dia', 'depth', 'pressure', 'len', 'geom')


# @admin.register(gis_model.RiserShapeModel)
# class RiserShapeModel(admin.ModelAdmin):
#     list_display = ('id', 'dia', 'pressure', 'no_of_burn', 'load_conne', 'pressure_o', 'mon_load', 'geom')


@admin.register(gis_model.ValvePitShapeModel)
class ValvePitShapeModel(admin.ModelAdmin):
    list_display = ('id', 'depth', 'geom')


@admin.register(gis_model.EndCapModel)
class EndCapModel(admin.ModelAdmin):
    list_display = ('id', 'geom')


@admin.register(gis_model.ReducerModel)
class ReducerModel(admin.ModelAdmin):
    list_display = ('id', 'geom')

class RiseShapeAdmin(LeafletGeoAdmin):
    pass
admin.site.register(gis_model.RiserShapeModel,RiseShapeAdmin)

admin.site.register(gis_model.FootPathShapeModel)