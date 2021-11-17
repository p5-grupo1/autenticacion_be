from django.contrib import admin
from django.urls    import path
from auth_app       import views
from rest_framework_simplejwt.views   import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',  TokenObtainPairView.as_view()),
    path('refresh/',    TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('user/',   views.UserCreateView.as_view()),
    path('user/<int:pk>/',  views.UserDetailView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view())
]
