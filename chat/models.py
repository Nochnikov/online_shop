from django.contrib.auth import get_user_model
from django.db import models


class Chat(models.Model):
    conversation_started_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(get_user_model(), related_name='chats')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
