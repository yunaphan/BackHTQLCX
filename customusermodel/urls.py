from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from accounts.views import (
    LogoutView, LoginView, Tokenuser, ListUserView, RetriveUserView, RegisterView, NhomThiCongView
)
from accounts.Api import (
    CayXanhApi, TenCXApi, TrangThaiCXApi,
    HinhThucThiCongApi, QuanHuyenPhuongXaApi,
    DuongApi, HinhAnhCayXanhApi, TrangThaiTCApi, LichThiCongApi,
    ChiTietLichThiCongApi,
    PhanQuyenApi
)
from accounts.Api.admin import (ThongTinNguoiDungTheoToken)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'user-list', ListUserView, base_name='Danh sách người dùng')
router.register(r'user', RetriveUserView, base_name='Chi tiết cập nhật thông tin người dùng')
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
router.register(r'chi-tiet-lich-thi-cong', ChiTietLichThiCongApi.ChiTietLichThiCongView, base_name="Chi tiết lịch thi công")
router.register(r'nhom-thi-cong', NhomThiCongView, base_name="Nhóm thi công")
router.register(r'chuc-nang', PhanQuyenApi.ChucNangView, base_name="Chức năng")
router.register(r'quyen-nguoi-dung', PhanQuyenApi.QuyenNguoiDungView, base_name="Quyền người dùng")
router.register(r'chuc-nang-nguoi-dung', PhanQuyenApi.ChucNangNguoiDungView, base_name="Chức năng người dùng")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', csrf_exempt(LoginView.as_view()), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', RegisterView.as_view(), name="đăng kí người dùng"),
    path('infomations-by-token/', ThongTinNguoiDungTheoToken.InformationsByToken.as_view(), name='Thông tin người dùng từ token'),
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

