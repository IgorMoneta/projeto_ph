from .services import UserService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class RegisterView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        cpf = request.data.get('cpf')
        birthday = request.data.get('birthday')

        userdata = {
            "username" : username,
            "password" : password,
            "email" : email,
            "first_name" : first_name,
            "last_name" : last_name,
            "cpf": cpf,
            "birthday": birthday
        }

        user = UserService.create_user(userdata)
        return Response(
            {"id": user.id , "email": user.email},
            status=status.HTTP_201_CREATED
            )