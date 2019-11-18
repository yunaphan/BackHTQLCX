from rest_framework.views import APIView
from accounts.permissions import IsAdmin
from rest_framework import permissions, viewsets
from accounts.Serializers.TrangThaiTCSerializer import TrangThaiThiCongSerializer
from accounts.models import Trangthaitc

class TrangThaiThiCongView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Trangthaitc.objects.all()
    serializer_class = TrangThaiThiCongSerializer
    lookup_field = "matrangthaitc"

# class TrangThaiThiCongView(APIView):
#     permission_classes = (permissions.IsAuthenticated, IsAdmin)
#     # queryset = models.Trangthaitc.objects.using("DoThi").all()
#     # serializer_class = TrangThaiTCSerializer
#     def post(self, request):
#         serializer = TrangThaiTCSerializer(data=request.data)
#         if serializer.is_valid():
#             self.object = serializer.save()
#             return response.Response("Tạo thành công", status=status.HTTP_201_CREATED, )
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)