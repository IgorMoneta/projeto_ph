from rest_framework import serializers

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,min_length=8)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    cpf = serializers.CharField()
    birthday = serializers.DateField()

class CreateUserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
   