from django.contrib.auth import get_user_model, user_logged_in
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from user.renderers import UserJSONRenderer
from user.serializers import LoginSerializer, RegistrationSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request, *args, **kwargs):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=user_data["email"]).first()
        user_logged_in.send(sender=type(user), request=request, user=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
