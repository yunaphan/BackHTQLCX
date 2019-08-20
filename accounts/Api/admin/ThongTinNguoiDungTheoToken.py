from rest_framework.views import APIView
from accounts.models import MyUser
from django.contrib.auth import get_user_model
from rest_framework import response, status
from rest_framework.authtoken.models import Token
User = get_user_model()

class InformationsByToken(APIView):
    def get_queryset(self):
        return Token.objects.values("user", "key")

    def post(self, request):
        queryset = self.get_queryset()
        get_token = request.data['key']
        # if not get_token:
        #     return response.Response({'error': 'Does not token'}, status=status.HTTP_204_NO_CONTENT)
        for user in queryset:
            if user['key'] == get_token:
                user_info = User.objects.values('id', 'username', 'gioitinh', 'ngaysinh', 'diachi',
                                                'email', 'noti_token', 'is_admin',
                                                'is_staff', 'is_active').get(id=user["user"])
                return response.Response(user_info)