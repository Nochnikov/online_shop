from django.shortcuts import render
from chat.models import Message, Chat
from rest_framework import generics
from chat.serializers import ChatSerializer, MessageSerializer
from shop.models import Product


# Create your views here.


class ListCreateChatView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        seller_id = Product.objects.get(pk=product_id).seller_id
        user = self.request.user
        users = serializer.validated_data['users']

        for user in users:
            users.remove(user)
            users.append(seller_id)

        users.append(user)

        serializer.save()

    def get_queryset(self):
        qs = Chat.objects.all().filter(users=self.request.user)
        return qs


class CreateListMessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        qs = Message.objects.all().filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save()
