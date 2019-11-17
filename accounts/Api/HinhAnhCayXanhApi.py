from accounts.Serializers.HinhAnhSerializer import HinhAnhCayXanhSerializer
# from accounts.Models.HinhAnhCXModel import Hinhanhcayxanh
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets, response, status
from rest_framework import permissions
from accounts.permissions import IsAdmin
from django.db import connection
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

class HinhAnhCayXanhView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    # queryset = HINHANHCAYXANH.objects.using('DoThi').all()
    # serializer_class = HinhAnhCayXanhSerializer

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = HinhAnhCayXanhSerializer(data=request.data)
        if serializer.is_valid():
            self.object = serializer.save(using='DoThi')
            return response.Response("Tạo thành công", status=status.HTTP_201_CREATED, )
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)