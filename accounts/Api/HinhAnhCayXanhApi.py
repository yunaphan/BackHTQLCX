from accounts.Serializers.HinhAnhSerializer import HinhAnhCayXanhSerializer
from rest_framework import response, status
from rest_framework import permissions, viewsets
from accounts.permissions import IsAdmin
from accounts.models import Hinhanhcayxanh
from rest_framework.views import APIView
from django.db import connections
from django.http import JsonResponse

class HinhAnhCayXanhView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Hinhanhcayxanh.objects.all()
    serializer_class = HinhAnhCayXanhSerializer
    lookup_field = "maanh"

# class DsHinhAnhCayXanhView(APIView):
#     permission_classes = (permissions.IsAuthenticated, IsAdmin)
#
#     def get(self, request):
#         ref = connections.cursor()
#         hinhanhcayxanh = ref.execute("Select * from sde.HINHANHCAYXANH")
#         serializer = (hinhanhcayxanh)
#         return JsonResponse(serializer, safe=False)
#
# class ThemHinhAnhCayXanhView(APIView):
#     permission_classes = (permissions.IsAuthenticated, IsAdmin)
#
#     def post(self, request, format=None):
#         serializer = HinhAnhCayXanhSerializer(data=request.data)
#         if serializer.is_valid():
#             self.object = serializer.save(using='DoThi')
#             return response.Response("Tạo thành công", status=status.HTTP_201_CREATED, )
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
