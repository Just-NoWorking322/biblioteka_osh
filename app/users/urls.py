from .views import ReadBookUploadView, UserRegister, IncreaseUserRatingView, CustomTokenObtainPairView, LogoutView, CategoryListView, SendEmailConfirmationView, SendPasswordResetCodeView, PasswordResetConfirmView, UserCabinetView, GoogleLoginAPIView, GoogleIDTokenLoginAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'register', UserRegister, basename='register')
router.register(r'raiting', IncreaseUserRatingView, basename='raiting')

urlpatterns = [
    path('read-book/', ReadBookUploadView.as_view(), name='read-book'),
    path('refresh/', TokenRefreshView.as_view(), name="api_user_refresh"),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('categories/', CategoryListView.as_view(), name='categories'), 
    path('', include(router.urls)),
    path('send-confirmation/', SendEmailConfirmationView.as_view(), name='send-email-confirmation'),
    path('password-reset/send-code/', SendPasswordResetCodeView.as_view(), name='password-reset-send-code'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('cabinet/', UserCabinetView.as_view(), name='user-cabinet'),
    path('google-login/', GoogleLoginAPIView.as_view(), name='google-login'),
    path('auth/google-id-token/', GoogleIDTokenLoginAPIView.as_view(), name='google-id-token-login'),
]
