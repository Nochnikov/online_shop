from django.shortcuts import render
from chat.models import Message, Chat
from rest_framework import generics
from chat.serializers import ChatSerializer, MessageSerializer
from shop.models import Product


# Create your views here.


class ListCreateChatView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        qs = Chat.objects.all().filter(user=self.request.user)
        return qs



class CreateListMessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        qs = Message.objects.all().filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')

        seller_id = Product.objects.get(pk=product_id).seller_id

        serializer.save(cutsomer=self.request.user, seller=seller_id)

