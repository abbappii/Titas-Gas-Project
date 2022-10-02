
from django.contrib import admin
from GIS_APP import models as gis_model
from leaflet.admin import LeafletGeoAdmin 


admin.site.register(gis_model.PlotShapeModel,LeafletGeoAdmin) 


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

class RiserAdmin(LeafletGeoAdmin):
    list_display = ['customerid']
    search_fields = ['customerid']
    list_filter = ['customerid']

admin.site.register(gis_model.RiserShapeModel,RiserAdmin)


admin.site.register(gis_model.FootPathShapeModel,LeafletGeoAdmin)

admin.site.register(gis_model.CasingModel, LeafletGeoAdmin)

# drs schema 
admin.site.register(gis_model.DRS, LeafletGeoAdmin)