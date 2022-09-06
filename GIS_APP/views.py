from django.core.serializers import serialize
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from rest_framework.response import Response

from GIS_APP import models as gis_model, serializer as gis_ser


# Create your views here.
# @login_required(login_url='auth_app:login')
def MapIndexView(request):
    return render(request, 'map_view.html', context={})


@login_required(login_url='auth_app:login')
def PlotInfoApiView(request):
    """
    Geo json response plot information
    """
    plot = gis_model.PlotShapeModel.objects.all()
    data = serialize('geojson', plot)
    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def RoadShapeInfoApiView(request):
    """
    Geo json response plot information
    """
    search = request.GET.get('search')
    if search:
        plot = gis_model.RoadShapeModel.objects.filter(Q(road_no__icontains=search))
    else:
        plot = gis_model.RoadShapeModel.objects.all()

    data = serialize('geojson', plot)

    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def GasLineInfoApiView(request):
    """
    Geo json response Gasline information
    """
    search = request.GET.get('search')
    if search:
        gasLine = gis_model.GasLineShapeModel.objects.filter(Q(dia__exact=search))
    else:
        gasLine = gis_model.GasLineShapeModel.objects.all()
    data = serialize('geojson', gasLine)
    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def RiserApiView(request):
    """
    Geo json response riser information
    """
    plot = gis_model.RiserShapeModel.objects.all()
    data = serialize('geojson', plot)
    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def ValvePitApiView(request):
    """
    Geo json response plot information
    """
    plot = gis_model.ValvePitShapeModel.objects.all()
    data = serialize('geojson', plot)
    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def EndCapApiView(request):
    """
    Geo json response plot information
    """
    plot = gis_model.EndCapModel.objects.all()
    data = serialize('geojson', plot)
    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def ReducerApiView(request):
    """
    Geo json response plot information
    """
    plot = gis_model.ReducerModel.objects.all()
    data = serialize('geojson', plot)
    return HttpResponse(data, content_type='json')


@login_required(login_url='auth_app:login')
def FootpathApiView(request):
    """
    Geo json response footpath information
    """
    plot = gis_model.FootPathShapeModel.objects.all()
    data = serialize('geojson', plot)
    return HttpResponse(data, content_type='json')


class GasLineInformationView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = gis_ser.GasPipelineSerializer
    queryset = gis_model.GasLineShapeModel.objects.all()

    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset().order_by('dia'), many=True).data
        dia_dict = []
        dia_lst = []
        x_val = []
        y_val = []
        whole = 0
        for i in data:
            if i['dia'] not in dia_lst:
                total = 0
                count = 0
                for new_data in data:

                    if new_data['dia'] == i['dia']:
                        count += 1
                        total += new_data['len']
                temp = {
                    'name': f"dia_{round(i['dia'], 2)}",
                    'dia': round(i['dia'], 2),
                    'total': round(total, 2),
                    'count': count
                }
                whole += total
                dia_dict.append(temp)
                dia_lst.append(i['dia'])
                y_val.append(total)
                x_val.append(f"dia-{round(i['dia'], 2)}")

        info = {
            'gas_line_dia_info': dia_dict,
            'x_val': x_val,
            'y_val': y_val,
            # 'gas_line_info': data,
        }
        return Response(info)


class GasLineFilterView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = gis_ser.GasPipelineSerializer

    def get_queryset(self):
        try:
            search = self.request.query_params.get('search')
            queryset = gis_model.GasLineShapeModel.objects.filter(Q(dia__exact=search))
        except:
            queryset = gis_model.GasLineShapeModel.objects.all()
        return queryset


class LineInformationView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = gis_ser.GasPipelineSerializer

    def get_queryset(self):
        search = self.kwargs['id']
        queryset = gis_model.GasLineShapeModel.objects.filter(id=search)
        return queryset


class RiserInformationView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = gis_ser.RiserSerializer

    def get_queryset(self):
        search = self.kwargs['id']
        queryset = gis_model.RiserShapeModel.objects.filter(id=search)
        return queryset


# class CasingView(generics.ListAPIView):
#     # permission_classes = [ permissions.IsAuthenticated]
#     serializer_class = gis_ser.CasingSerializer
#     def get_queryset(self):
#         search = self.kwargs['id']
#         queryset = gis_model.CasingModel.objects.filter(id=search)
#         return queryset

@login_required(login_url='auth_app:login')
def CasingView(request):
    """
    Geo json response plot information
    """
    qs = gis_model.CasingModel.objects.all()
    data = serialize('geojson', qs)
    return HttpResponse(data, content_type='json')
