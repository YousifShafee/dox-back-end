from main.general_fun import get_data_by_field
from rest_framework import generics, authentication
from rest_framework.views import APIView
from datetime import date, datetime
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login as auth_login, logout
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from datetime import date
from .serializers import *
from main.models import User

model_name = User
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_at=date.today())


class UserList(generics.ListAPIView):
    queryset = model_name.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]


def delete(request):
    return UserDetails.as_view(**{'user_id': request.user.id})(request)


class UserDetails(generics.RetrieveAPIView):
    queryset = model_name.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserDelete(generics.DestroyAPIView):
    queryset = model_name.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]


class UserUpdate(APIView):
    queryset = model_name.objects.all()
    serializer_class = EditSerializer

    def post(self, request, pk):
        serializer = EditSerializer.validate(self, data=request.data, pk=pk)
        if serializer:
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)
        

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = UserLoginSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self,
        }

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer.validate(self, data=request.data)

        if serializer:
            user = serializer['user'] or request.user
            token = serializer['token']
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            login(request)
            response.data['id'] = user.id
            response.data['email'] = user.email
            response.data['mission'] = user.mission
            return response

        return Response("Incorrect credentials, Please Try Again", status=HTTP_400_BAD_REQUEST)


def login(request):
    msg = []
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return msg.append("login successful")
        else:
            return msg.append("disabled account")
    else:
        return msg.append("invalid login")


class Logout(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        logout(request)
        return Response(status=HTTP_200_OK)

class ConfirmAccount(APIView):
    permission_classes = [AllowAny]
    serializer_class = ConfirmAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = ConfirmAccountSerializer.validate(self, data=request.data)
        if serializer:
            return Response(serializer, status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)


class SendCode(APIView):
    permission_classes = [AllowAny]
    serializer_class = SendCodeSerializer
    
    def post(self, request):
        serializer = SendCodeSerializer.validate(self, data=request.data)
        if serializer:
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)


class ChangePass(generics.RetrieveUpdateAPIView):
    queryset = model_name.objects.all()
    serializer_class = ChangePassSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ChangePassSerializer.validate(self, data=request.data)
        if serializer:
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_404_NOT_FOUND)


class UserSearch(APIView):
    queryset = model_name.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        q = get_data_by_field(request.data, search_dict)
        if q is {}:
            model_data = model_name.objects.all()
        else:
            model_data = model_name.objects.filter(**q)
        result = UsersSerializer(model_data, many=True).data
        return Response(result)


search_dict = {
    'first_name': 'first_name__contains',
    'last_name': 'last_name__contains',
}