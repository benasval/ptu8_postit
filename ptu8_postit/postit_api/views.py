from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from . import models, serializers


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def delete(self, request, *args, **kwargs):
        obj = self.queryset.filter(pk=kwargs['pk'], user=self.request.user)
        if obj.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('Object not found or does not belong to you.'))

    def put(self, request, *args, **kwargs):
        obj = self.queryset.filter(pk=kwargs['pk'], user=self.request.user)
        if obj.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('Object not found or does not belong to you.'))
