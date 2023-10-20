from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status, viewsets
from .models import DentalProfile
from .serializers import DentalProfileSerializer


class UserSignUp(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = request.data
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserSignIn(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)

	def post(self, request):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserSignOut(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserDetailView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)

class DentalProfileView(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	serializer_class = DentalProfileSerializer
	action_serializers = {
        "retrieve": DentalProfileSerializer,
        "dafault": DentalProfileSerializer,
        "update": DentalProfileSerializer,
    }
	queryset = DentalProfile.objects.all()
    