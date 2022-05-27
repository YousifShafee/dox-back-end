from rest_framework.serializers import ModelSerializer
from main.models import User
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
)

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class UserCreateSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email')
    password = CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'token',
            'first_name',
            'last_name',
            'email',
            'password',
            'gender',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This Email has already registered.")
        username = data['username']
        password = data['password']
        user_na = User.objects.filter(username=username)
        if user_na.exists():
            raise ValidationError("This Username has already Used.")
        if username == password:
            raise ValidationError("Password Can't be equal to Username.")
        if len(password) < 8:
            raise ValidationError("Password Can't be less than 8 character.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        gender = validated_data['gender']
        user_obj = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )
        user_obj.set_password(password)
        user_obj.save()
        user_qs = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        payload = jwt_payload_handler(user)
        validated_data['token'] = jwt_encode_handler(payload)
        validated_data['id'] = user_qs.id
        validated_data['password'] = '*****'
        del validated_data['first_name']
        del validated_data['last_name']
        del validated_data['gender']
        result = {'token': jwt_encode_handler(payload), 'user': user}
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True, required=False, label='Username')
    password = CharField(allow_blank=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id',
            'token',
            'username',
            'password'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data.get('username')
        password = data['password']

        if not username:
            raise ValidationError("The Username is required")
        user = User.objects.get(username=username)
        if user :
            if not user.check_password(password):
                raise ValidationError("Incorrect credentials, Please Try Again")
        else:
            raise ValidationError("This Username not valid")

        user = authenticate(username=username, password=password)
        payload = jwt_payload_handler(user)
        result = {'token': jwt_encode_handler(payload), 'user': user}
        return result


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'gender',
            'last_login',
        ]


class UsersNameDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AllDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'gender']