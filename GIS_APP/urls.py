from django.urls import path
from GIS_APP import views as gis_view

app_name = 'gis_app'
urlpatterns = [
    path('map/', gis_view.MapIndexView, name='index_page'),
    # API urls
    path('api/plot_info/', gis_view.PlotInfoApiView, name='plot_info_api'),
    path('api/road_shape/', gis_view.RoadShapeInfoApiView, name='road_shape_info_api'),
    path('api/gas_line_info/', gis_view.GasLineInfoApiView, name='gas_line_info_api'),
    path('api/valvepit_api/', gis_view.ValvePitApiView, name='valvepit_info_api'),
    path('api/end_cap/', gis_view.EndCapApiView, name='end_capinfo_api'),
    path('api/reducer_info/', gis_view.ReducerApiView, name='reducer_info_api'),
    path('api/footpath/', gis_view.FootpathApiView, name='footpath_api'),
    path('api/riser/', gis_view.RiserApiView, name='riser_info_api'),
    path('api/riser/<id>/', gis_view.RiserInformationView.as_view(), name='riser_information_api'),
    path('api/casing/', gis_view.CasingView, name='casing_info_api'),

    # Gasline information
    path('api/pipe_line_info/', gis_view.GasLineInformationView.as_view(), name='pipe_line_info'),
    path('api/pipe_line_filter/', gis_view.GasLineFilterView.as_view(), name='pipe_line_filter'),
    path('api/pipe_line_info/<id>/', gis_view.LineInformationView.as_view(), name='pipe_line_info_filter'),
]
