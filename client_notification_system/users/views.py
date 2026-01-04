from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            errors = {}
            
            # Check if username already exists
            if User.objects.filter(username=data['username']).exists():
                errors['username'] = 'User already exists'
            
            # Check if email already exists
            if User.objects.filter(email=data['email']).exists():
                errors['email'] = 'Email is already in use.'
            
            if errors:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
