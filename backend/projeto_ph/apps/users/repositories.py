from .models import Usuario
from django.contrib.auth.hashers import make_password

class UserRepository:

    def create_user(data):
        usuario = Usuario.objects.create(
        username=data["username"],
        email=data["email"],
        password=make_password(data["password"])
        )
        return usuario
    
    def get_all():
        pass
    def get_user_by_id(id):
        pass
    def delete_user(id):
        pass
    def get_user_by_user(username):
        if Usuario.objects.filter(username=username).exists():
            return True