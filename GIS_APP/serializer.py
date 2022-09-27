from rest_framework import serializers
from GIS_APP import models as gis_model


class GasPipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = gis_model.GasLineShapeModel
        exclude = ['geom']


class RiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = gis_model.RiserShapeModel
        fields = '__all__'
        # exclude = ['geom']

# def to_representation(self, instance):
#     data = super(GasPipelineSerializer, self).to_representation(instance)
#     print('dddd' ,data.get('dia'))
#     return data

class CasingSerializer(serializers.ModelSerializer):
    class Meta:
        model = gis_model.CasingModel
        fields = '__all__'


class ValvepitlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = gis_model.ValvePitShapeModel
        exclude = ['geom']


class DrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = gis_model.DRS
        fields = '__all__'