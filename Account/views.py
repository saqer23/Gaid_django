from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.views import APIView
from .models import Profile
from .serializer import RegisterSerializer,UpdateSerializer,UserSerializer,UpdateProfileSerializer



@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })




@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response({
        'error':'not authenticated',
    },status=400)



# @api_view(['PUT'])
# def update_user_data(request):
#     user = request.user
#
#     if user.is_authenticated:
#         serializer = UpdateSerializer(user,data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user = serializer.save()
#
#         _, token = AuthToken.objects.create(user)
#         return Response({
#             'user_info': {
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email,
#                 'first_name':user.first_name,
#                 'last_name':user.last_name,
#             },
#         })
#     return Response({
#         'error':'not authenticated',
#     },status=400)


@api_view(['PUT'])
def update_profile_data(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if user.is_authenticated:
        serializer = UpdateProfileSerializer(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        profile.img_profile = request.FILES.get('img_profile')
        profile.save()
        user = serializer.save()
        # _, token = AuthToken.objects.create(user)
        return Response(serializer.data)
        # return Response({
        #     'user_info': {
        #         'id': user.id,
        #         'username': user.username,
        #         'email': user.email,
        #         'asss':serializer.data
        #     },
        # },)
    return Response({
        'error':'not authenticated',
    },status=400)


