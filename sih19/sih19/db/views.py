from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics

# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer


class RegionListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Region.objects.all()
	serializer_class = serializers.RegionSerializer


class RegionUpdateAPIView(generics.UpdateAPIView):
	queryset = models.Region.objects.all()
	serializer_class = serializers.RegionSerializer


class ReportListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Report.objects.all()
	serializer_class = serializers.ReportSerializer


class WaterbodyReportListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.WaterbodyReport.objects.all()
	serializer_class = serializers.WaterbodyReportSerializer


class PredictListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Predict.objects.all()
	serializer_class = serializers.PredictSerializer


class HospitalListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Hospital.objects.all()
	serializer_class = serializers.HospitalSerializer


class HospitalCurrentListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.HospitalCurrent.objects.all()
	serializer_class = serializers.HospitalCurrentSerializer


class HeatmapActualListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.HeatmapActual.objects.all()
	serializer_class = serializers.HeatmapActualSerializer


class HeatmapPredictedListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.HeatmapPredicted.objects.all()
	serializer_class = serializers.HeatmapPredictedSerializer


class NewsListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.News.objects.all()
	serializer_class = serializers.NewsSerializer


class LabListCreateAPIView(generics.ListCreateAPIView):
	queryset = models.Lab.objects.all()
	serializer_class = serializers.LabSerializer


