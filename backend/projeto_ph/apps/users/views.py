from .services import UserService
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CreateUserResponseSerializer, CreateUserSerializer
class CreateUserView(APIView):
    
    def post(self, request):
        # username = request.data.get('username')
        # password = request.data.get('password')
        # email = request.data.get('email')
        # first_name = request.data.get('first_name')
        # last_name = request.data.get('last_name')
        # cpf = request.data.get('cpf')
        # birthday = request.data.get('birthday')

        # userdata = {
        #     "username" : username,
        #     "password" : password,
        #     "email" : email,
        #     "first_name" : first_name,
        #     "last_name" : last_name,
        #     "cpf": cpf,
        #     "birthday": birthday
        # }
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.create_user(serializer.validated_data)
        
        return Response(
            CreateUserResponseSerializer(user).data,
            status=status.HTTP_201_CREATED
            )
    