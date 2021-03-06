from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from accounts.models import NhomThiCong
from accounts.Serializers.ChiTietLichThiCongSerializer import ChiTietLichThiCongSerializer
import bcrypt
User = get_user_model()

class UserCreationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(read_only=True)
    noti_token = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, required=False)
    middlename = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, required=False)
    # duongdanavatar = serializers.FileField(allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'gioitinh', 'ngaysinh', 'diachi', 'email',
                  'password', 'password2', 'noti_token', 'is_admin', 'is_staff',
                  'is_active', 'phone', 'firstname', 'lastname',
                  'middlename', 'duongdanavatar', 'nhomthicong', 'quyen']

    def create(self, validated_data):
        algorithm = "bcrypt"
        digest = None
        library = ("bcrypt", "bcrypt")
        rounds = 10
        username = validated_data["username"]
        password = validated_data["password"].encode('utf8')
        validated_data["password"] = algorithm + '$' + bcrypt.hashpw(password, bcrypt.gensalt(10)).decode()
        # token, created = Token.objects.get_or_create(user=username)
        return User.objects.create(**validated_data)


class NhomTCSerializer(serializers.ModelSerializer):
    thanhviennhomthicong = UserCreationSerializer(many=True, read_only=True)
    # nhomthiconglich = ChiTietLichThiCongSerializer(many=True, read_only=True)

    class Meta:
        model = NhomThiCong
        fields = ('manhomthicong', 'tennhomthicong', 'thanhviennhomthicong')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Incorrect username or password!')
        if not user.is_active:
            raise serializers.ValidationError('User is disabled!')
        return {'user': user}

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("user", "auth_token", "created")

# class CayXanhTTSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TINHTRANG_CAYXANH
#         fields = ('objectid_id', 'matinhtrang_id')