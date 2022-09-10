# from django import forms
# from leaflet.forms import L

# class PointEntryOrSelectForm(forms.ModelForm):
#     lat = forms.FloatField(required=False, label='Latitude')
#     lng = forms.FloatField(required=False, label='Longtitude')

#     class Meta:
#         widgets = {'geom': LeafletWidget()}
#         model = ' '
#         exclude = ['', ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         geom = self.initial.get("geom", None)
#         if isinstance(geom, Point):
#             self.initial["lng"], self.initial["lat"] = geom.tuple

#     def clean(self):
#         data = super().clean()
#         if set(self.changed_data)>={"lat","lng"}:
#             lat, lng = data.pop("lat", None), data.pop("lng", None)
#             data["geom"] = Point(lng, lat, srid=4326)
    
#         if not (data["geom"] or (data["lat"] and data["lng"])):
#             raise forms.ValidationError(
#                 {"geom": "No coordinates."})
#         return data

 