from rest_framework                         import serializers
from auth_app.models.user                   import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'email', 'rol_jardinero', 'descripcion', 'ciudad', 'telefono']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'nombre'  : user.nombre,
            'email'   : user.email,
            'rol_jardinero'  : user.rol_jardinero,
            'descripcion'    : user.descripcion,
            'ciudad'         : user.ciudad,
            'telefono'       : user.telefono
        }