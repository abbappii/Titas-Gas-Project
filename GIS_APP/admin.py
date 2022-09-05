from re import L
from django.contrib import admin
from GIS_APP import models as gis_model
from leaflet.admin import LeafletGeoAdmin 


admin.site.register(gis_model.PlotShapeModel,LeafletGeoAdmin) 


# @admin.register(gis_model.RoadShapeModel)
# class RoadShapeModel(admin.ModelAdmin):
#     list_display = ('id', 'road_no', 'geom')

admin.site.register(gis_model.RoadShapeModel,LeafletGeoAdmin)
# @admin.register(gis_model.GasLineShapeModel)
# class GasLineShapeModel(admin.ModelAdmin):
#     list_display = ('id', 'dia', 'depth', 'pressure', 'len', 'geom')

admin.site.register(gis_model.GasLineShapeModel,LeafletGeoAdmin)

admin.site.register(gis_model.ValvePitShapeModel, LeafletGeoAdmin)


admin.site.register(gis_model.EndCapModel, LeafletGeoAdmin) 


admin.site.register(gis_model.ReducerModel, LeafletGeoAdmin)

class RiserShapeAdmin(LeafletGeoAdmin):
    pass
admin.site.register(gis_model.RiserShapeModel,RiserShapeAdmin) 

admin.site.register(gis_model.FootPathShapeModel,LeafletGeoAdmin)

admin.site.register(gis_model.CasingModel, LeafletGeoAdmin)