from django.urls import path
from .views import UserRegisterView, UserDetailView, AddFriendView, RemoveFriendView, MessageCreateView, MessageListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/add_friend/', AddFriendView.as_view(), name='add-friend'),
    path('user/<int:pk>/remove_friend/', RemoveFriendView.as_view(), name='remove-friend'),
    path('messages/', MessageCreateView.as_view(), name='send-message'),
    path('messages/inbox/', MessageListView.as_view(), name='inbox'),
]
