from django.urls import path
from rest_framework import routers
from chat.views import ListCreateChatView,  CreateListMessageView

urlpatterns = [
    path('list/', ListCreateChatView.as_view(), name='chat_list'),
    path('list/create/', ListCreateChatView.as_view(), name='chat_create'),

    #messsage

    path('messages/', CreateListMessageView.as_view(), name='messages_list'),
    path('messages/<int:product_id>/', CreateListMessageView.as_view(), name='messages_create'),

]