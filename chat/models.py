from django.contrib.auth import get_user_model
from django.db import models


class Chat(models.Model):
    conversation_started_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(get_user_model(), related_name='chats')

class Message(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='customer_messages')
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='seller_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
