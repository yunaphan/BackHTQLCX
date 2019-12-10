from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from accounts.Serializers.CayXanhSerializer import CayXanhserializer
from accounts.Models.CayXanhModel import Cayxanh
from rest_framework import permissions
from accounts.permissions import IsAdmin

class CayXanhView(viewsets.GenericViewSet, ListAPIView, CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = CayXanhserializer
    queryset = Cayxanh.objects.values('objectid', 'sohieu', 'matencx', 'matinhtrang', 'kinhdo', 'vido', 'duongkinh',
                  'chieucao', 'dorongtan', 'ngaytrong', 'ngaycapnhat', 'thuoctinh',
                  'ghichu', 'tuyenduong', 'phuongxa', 'quanhuyen', 'nguoicapnhat')

class CayXanhExportpdfView(viewsets.GenericViewSet, ListAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    serializer_class = CayXanhserializer
    queryset = Cayxanh.objects.values('objectid', 'sohieu', 'matencx', 'matinhtrang', 'kinhdo', 'vido', 'duongkinh',
                  'chieucao', 'dorongtan', 'ngaytrong', 'ghichu')

# class CayXanhTheoTenView(viewsets.GenericViewSet, ListAPIView):
#     permission_classes = (permissions.IsAuthenticated, IsAdmin)
#     serializer_class = CayXanhserializer
#     queryset = Cayxanh.objects.values('objectid', 'sohieu', 'matencx', 'kinhdo', 'vido', 'duongkinh',
#                                       'chieucao', 'dorongtan', 'ngaytrong', 'ghichu')