from django.http.request import validate_host
from rest_framework                         import status, views, generics
from rest_framework.response                import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer


from auth_app.models.user                   import User
from auth_app.serializers.userSerializer    import UserSerializer

from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.backends      import TokenBackend
from django.conf                            import settings 
from django_filters.rest_framework          import DjangoFilterBackend


class UserCreateView(views.APIView):
    """ 
    Servicio para crear usuario
    """
    def post(self, request, *args, **kwargs):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        token_data = {
            'username':request.data['username'],
            'password':request.data['password']
        }
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)


class UserDetailView(generics.RetrieveAPIView):
    """
    Servicio para listar la informacion de un usuario
    """
    queryset    = User.objects.all()
    serializer_class    = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self,request, *args, **kwargs)
        

class UserUpdateView(generics.UpdateAPIView):
    """
    Servicio para actualizar la informacion de un usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class UserListUsername(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset