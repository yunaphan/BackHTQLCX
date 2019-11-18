from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns
from accounts.views import (
    LogoutView, LoginView,
    RegisterView, Tokenuser
)
from accounts.Api import (
    CayXanhApi, TenCXApi, TrangThaiCXApi,
    HinhThucThiCongApi, QuanHuyenPhuongXaApi,
    DuongApi, HinhAnhCayXanhApi, TrangThaiTCApi, LichThiCongApi
)
from accounts.Api.admin import (ThongTinNguoiDungTheoToken)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'user', RegisterView, base_name='user')
router.register(r'token', Tokenuser, base_name='token')
router.register(r'cay-xanh', CayXanhApi.CayXanhView, base_name='cây xanh')
router.register(r'ten-cay-xanh', TenCXApi.TenCXView, base_name='tên cây xanh')
router.register(r'trang-thai-cay-xanh', TrangThaiCXApi.TrangThaiCayXanhView, base_name='trạng thái cây xanh')
router.register(r'hinh-thuc-thi-cong', HinhThucThiCongApi.HinhThucThiCongView, base_name='Hình Thức Thi Công cây xanh')
router.register(r'danh-muc-quan-huyen', QuanHuyenPhuongXaApi.QuanHuyenView, base_name='Danh mục quận huyện')
router.register(r'danh-muc-phuong-xa', QuanHuyenPhuongXaApi.PhuongxaView, base_name='Danh mục phường xã')
router.register(r'danh-muc-tuyen-duong', DuongApi.DuongView, base_name='Danh mục tuyến đường')
router.register(r'hinh-anh-cay', HinhAnhCayXanhApi.HinhAnhCayXanhView, base_name="Hình ảnh cây")
router.register(r'danh-muc-trang-thai-thi-cong', TrangThaiTCApi.TrangThaiThiCongView, base_name='Trạng thái thi công')
router.register(r'lich-thi-cong', LichThiCongApi.LichThiCongView, base_name="Lịch thi công")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', csrf_exempt(LoginView.as_view()), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('infomations-by-token/', ThongTinNguoiDungTheoToken.InformationsByToken.as_view(), name='Thông tin người dùng từ token'),
    path('', include(router.urls)),
    # path('hinh-anh-cay/', HinhAnhCayXanhApi.DsHinhAnhCayXanhView.as_view(), name="Danh sách hình ảnh cây"),
    # path('them-hinh-anh-cay/', HinhAnhCayXanhApi.ThemHinhAnhCayXanhView.as_view(), name="Thêm hình ảnh cây"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
