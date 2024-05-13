"""Module for authentication views"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from planttrackerapi.models import UserProfile
from planttrackerapi.serializers import UserProfileSerializer

@api_view(['post'])
@permission_classes([AllowAny])
def login(request):
    """Handle login request"""
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token, _ = Token.objects.get_or_create(user=authenticated_user)
        profile = UserProfile.objects.get(user=authenticated_user)
        serializer = UserProfileSerializer(profile, context={'request': request})
        return Response({'token': token.key,'user': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Handle registration request"""
    new_user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        password=request.data['password']
    )

    profile = UserProfile.objects.create(
        user=new_user,
        profile_image_url=request.data['profile_image_url'],
        zip_code=request.data['zip_code']
    )

    serializer = UserProfileSerializer(profile, context={'request': request})
    return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def change_password(request):
    """Handle password change request"""
    request.user.set_password(request.data['password'])
    request.user.save()

    return Response({}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def change_profile(request):
    """Handle profile change request"""
    profile = UserProfile.objects.get(user=request.user)
    profile.profile_image_url = request.data['profile_image_url']
    profile.zip_code = request.data['zip_code']
    profile.save()

    serializer = UserProfileSerializer(profile, context={'request': request})
    return Response({'user': serializer.data}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def logout(request):
    """Handle logout request"""
    request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
