from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):#Estos permisos es para cuando se actualicen los perfiles de usuario
    """Esta clase permite a que un usuario pueda editar/actualizar su propio perfil y no el de los demás"""

    def has_object_permission(self, request, view, obj):
        """Método para verificar si un usuario está intentando actualizar su propio perfil"""
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Se verifica si el obj a actualizar es igual al obj del request del usuario
        #De ser esto verdadero se cumplen los cambios que hizo el usuario
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Esta clase permitirá que un usuario realice un publicación o actualizar su feed"""

    def has_object_permission(self, request, view, obj):
        """Se verifica si el usuario está en su perfil y no el de otro usuario"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id