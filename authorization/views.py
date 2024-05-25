from django.contrib.auth.hashers import make_password
from rest_framework import generics, mixins
from authorization.serializers import RegisSerializer, ProfileSerializer

from authorization.models import User


# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisSerializer
    lookup_filed = 'pk'

    # To hash the password
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)


class ProfileView(generics.GenericAPIView,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):

    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self):
        instance = User.objects.get(pk=self.request.user.pk)
        return instance
