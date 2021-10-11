
from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserDetail, MyTokenObtainPairView, ChangePasswordView,UpdateProfileView

app_name = 'users'



urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('current_user/<int:pk>/', UserDetail.as_view(), name='current_user'),
    path('token/', MyTokenObtainPairView.as_view(), name='my_token'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),

]