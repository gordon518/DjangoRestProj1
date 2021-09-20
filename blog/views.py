# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import *

#login
class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.get(username__exact=username)
        if user.password == password:
            serializer = UserSerializer(user)
            new_data = serializer.data
            # save user to session
            self.request.session['user_id'] = user.id
            seesionUserid=request.session.get('user_id')
            return Response(new_data, status=HTTP_200_OK)
        return Response('password error', HTTP_400_BAD_REQUEST)

#register
class UserRegisterAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        username = data.get('username')
        if User.objects.filter(username__exact=username):
            return Response("Username already existed",HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#add, delete, modify, query function for blog. All function need permission except query
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        #print(self.request.user)
        serializer.save(owner=User.objects.get(id=self.request.session.get('user_id')))

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
