from email.policy import default
from main.general_fun import get_confirm_code
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
            'first_name',
            'last_name',
            'token',
            'email',
            'password',
            'phone',
            'gender',
            'mission',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data['email']
        data['username'] = data['email']
        password = data['password']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This Email has already registered.")
        if email == password:
            raise ValidationError("Password Can't be equal to Username.")
        if len(password) < 8:
            raise ValidationError("Password Can't be less than 8 character.")
        return data

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        phone = validated_data['phone']
        gender = validated_data['gender']
        mission = validated_data['mission']
        if mission == "Normal":
            active_code = get_confirm_code(email)
            is_active = False
        else:
            active_code = 0
            is_active = True
        user_obj = User(
            username=username,
            email=email,
            active_code=active_code,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            mission=mission,
            is_active=is_active
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email')
    password = CharField(allow_blank=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'id',
            'token',
            'email',
            'password',
            'mission',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get('email')
        password = data['password']
        mission = data['mission']
        if not email:
            raise ValidationError("The Username is required")
        user = User.objects.get(username=email)
        if user:
            if not user.check_password(password):
                raise ValidationError(
                    "Incorrect credentials, Please Try Again")
        else:
            raise ValidationError("This Username not valid")
        if not user.is_active:
            raise ValidationError("Not Active")
        if user.mission not in mission:
            raise ValidationError("Not Allowed")
        user = authenticate(username=email, password=password)
        payload = jwt_payload_handler(user)
        result = {'token': jwt_encode_handler(payload), 'user': user}
        return result


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'mission',
            'last_login',
        ]


class EditSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'password']

    def validate(self, data, pk):
        user = User.objects.get(id=pk)
        if 'password' in data:
            user.set_password(data['password'])
        else:
            user.phone = data['phone']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
        user.save()
        return True


class SendCodeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate(self, data):
        email = data['email']
        user = User.objects.get(email=email)
        if user:
            user.active_code = get_confirm_code(email)
            user.save()
            return True
        return False


class ConfirmAccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['code', 'email']

    def validate(self, data):
        user = User.objects.get(email=data['email'])
        if user:
            user.is_active = True
            user.save()
            return True
        return False


class ChangePassSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'email']

    def validate(self, data):
        user = User.objects.get(username=data['email'])
        if user:
            user.set_password(data['password'])
            user.save()
            return True
        return False
