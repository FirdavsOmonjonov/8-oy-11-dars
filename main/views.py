from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, Message
from .serializers import UserSerializer, MessageSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddFriendView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        friend = User.objects.get(pk=pk)
        user.friends.add(friend)
        user.save()
        return Response({"message": "Friend added"}, status=status.HTTP_200_OK)

class RemoveFriendView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        friend = User.objects.get(pk=pk)
        user.friends.remove(friend)
        user.save()
        return Response({"message": "Friend removed"}, status=status.HTTP_200_OK)

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(receiver=user)
