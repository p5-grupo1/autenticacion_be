from django.contrib import admin
from django.urls    import path, re_path
from auth_app       import views
from rest_framework_simplejwt.views   import (TokenObtainPairView, TokenRefreshView)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v0.1',
      description="Documentacion publica de API de Autenticacion",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cdospinav16@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',  TokenObtainPairView.as_view()),
    path('refresh/',    TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('user/',   views.UserCreateView.as_view()),
    path('user/<int:pk>/',  views.UserDetailView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]