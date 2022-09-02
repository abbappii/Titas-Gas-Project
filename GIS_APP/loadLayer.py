from django.contrib.gis.utils import LayerMapping
import os
import django
from GIS_APP import models as gis_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Narshindi_GIS.settings")
django.setup()
#
#
# Auto-generated `LayerMapping` dictionary for plot Shape Model
plot_mapping = {
    'plot': 'Plot',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for RoadShapeModel model
roadshapemodel_mapping = {
    'road_no': 'Road_No_',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for GasLineShapeModel model
gaslineshapemodel_mapping = {
    'dia': 'Dia',
    'depth': 'Depth',
    'len': 'Shape_Leng',
    'pressure': 'Pressure',
    'geom': 'MULTILINESTRING',
}

# raiser_mapping = {
#     'dia': 'dia',
#     'pressure': 'Pressure',
#     'cus_id': 'Cus_id',
#     'no_of_burn': 'No_of_burn',
#     'load_conne': 'load_conne',
#     'pressure_o': 'Pressure_o',
#     'mon_load': 'mon_load',
#     'geom': 'MULTIPOINT',
# }
raiser_mapping = {
    'customerid': 'CustomerID',
    'customer_1': 'Customer_1',
    'status_1': 'Status_1',
    'burner_typ': 'Burner_typ',
    'burner_no_field': 'Burner_no_',
    'customer_2': 'Customer_2',
    'customer_3': 'Customer_3',
    'status_2': 'Status_2',
    'burner_t_1': 'Burner_t_1',
    'burner_no1': 'Burner_no1',
    'customer_4': 'Customer_4',
    'customer_5': 'Customer_5',
    'status_3': 'Status_3',
    'burner_t_2': 'Burner_t_2',
    'burner_n_1': 'Burner_n_1',
    'customer_6': 'Customer_6',
    'customer_7': 'Customer_7',
    'status_4': 'Status_4',
    'burner_t_3': 'Burner_t_3',
    'burner_n_2': 'Burner_n_2',
    'customer_8': 'Customer_8',
    'customer_9': 'Customer_9',
    'status_5': 'Status_5',
    'burner_t_4': 'Burner_t_4',
    'burner_n_3': 'Burner_n_3',
    'custome_10': 'Custome_10',
    'custome_11': 'Custome_11',
    'status_6': 'Status_6',
    'burner_t_5': 'Burner_t_5',
    'burner_n_4': 'Burner_n_4',
    'custome_12': 'Custome_12',
    'custome_13': 'Custome_13',
    'status_7': 'Status_7',
    'burner_t_6': 'Burner_t_6',
    'burner_n_5': 'Burner_n_5',
    'custome_14': 'Custome_14',
    'custome_15': 'Custome_15',
    'status_8': 'Status_8',
    'burner_t_7': 'Burner_t_7',
    'burner_n_6': 'Burner_n_6',
    'custome_16': 'Custome_16',
    'custome_17': 'Custome_17',
    'status': 'Status',
    'burner_t_8': 'Burner_t_8',
    'burner_n_7': 'Burner_n_7',
    'custome_18': 'Custome_18',
    'custome_19': 'Custome_19',
    'status_10': 'Status_10',
    'burner_t_9': 'Burner_t_9',
    'burner_n_8': 'Burner_n_8',
    'burner_10': 'Burner__10',
    'burner_n_9': 'Burner_n_9',
    'burner_11': 'Burner__11',
    'burner_12': 'Burner__12',
    'burner_13': 'Burner__13',
    'burner_14': 'Burner__14',
    'burner_15': 'Burner__15',
    'burner_16': 'Burner__16',
    'burner_17': 'Burner__17',
    'burner_18': 'Burner__18',
    'burner_19': 'Burner__19',
    'burner_20': 'Burner__20',
    'burner_21': 'Burner__21',
    'burner_22': 'Burner__22',
    'burner_23': 'Burner__23',
    'burner_24': 'Burner__24',
    'burner_25': 'Burner__25',
    'burner_26': 'Burner__26',
    'burner_27': 'Burner__27',
    'burner_28': 'Burner__28',
    'total_load': 'Total_Load',
    'pressure_o': 'Pressure_O',
    'geom': 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for ValvePitShapeModel model
ValvePitShapeModel_mapping = {
    'geom': 'MULTIPOINT',
}

valvepit_mapping = {
    'depth': 'depth',
    'pressure': 'pressure',
    'valve_type': 'valve_type',
    'geom': 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for EndCapModel model
endcapmodel_mapping = {
    'geom': 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for ReducerModel model
reducermodel_mapping = {
    'geom': 'MULTIPOINT',
}

footpath_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}


# # loc_shape = os.path.abspath('E:\Pranto\Storage\SHAPEFILE')
# loc_shape = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/SHAPEFILE/CL_RS/'))
# loc_shape = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ShapeFile/plotShape/riser/19_06_22/'))

loc_shape = os.path.abspath(os.path.join(os.path.dirname(__file__),'ShapeFile/NewPlotShape/Plot/'))
loc_shape_road = os.path.abspath(os.path.join(os.path.dirname(__file__),'ShapeFile/NewPlotShape/Road/'))
loc_shape_gas = os.path.abspath(os.path.join(os.path.dirname(__file__),'ShapeFile/NewPlotShape/GasLine/'))


def run(verbose=True):
    lm = LayerMapping(gis_model.PlotShapeModel, loc_shape, plot_mapping, transform=False,
                      encoding='iso-8859-1')
    # lm = LayerMapping(geo_model.RsShapeFieldModel, loc_shape, gis_mapping_rs, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def run_road(verbose=True):
    lm = LayerMapping(gis_model.RoadShapeModel, loc_shape_road, roadshapemodel_mapping, transform=False,
                      encoding='iso-8859-1')
    # lm = LayerMapping(geo_model.RsShapeFieldModel, loc_shape, gis_mapping_rs, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runGasLine(verbose=True):
    lm = LayerMapping(gis_model.GasLineShapeModel, loc_shape_gas, gaslineshapemodel_mapping, transform=False,
                      encoding='iso-8859-1')
    # lm = LayerMapping(geo_model.RsShapeFieldModel, loc_shape, gis_mapping_rs, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)