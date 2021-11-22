from django.http.request import validate_host
from rest_framework                         import status, views, generics
from rest_framework.response                import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer


from auth_app.models.user                   import User
from auth_app.serializers.userSerializer    import UserSerializer

from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.backends      import TokenBackend
from django.conf                            import settings 


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
    permissions_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token   = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend   = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        validate_data   = token_backend.decode(token, verify=False)

        if validate_data['user_id'] != kwargs['pk']:
            string_response =   {'detail': "Acceso no Autorizado."}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(self,request, *args, **kwargs)

class UserUpdateView(generics.UpdateAPIView):
    """
    Servicio para actualizar la informacion de un usuario
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permissions_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        token   = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend   = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        validate_data   = token_backend.decode(token, verify=False)

        if validate_data['user_id'] != kwargs['pk']:
            string_response =   {'detail': "Acceso no Autorizado."}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)
