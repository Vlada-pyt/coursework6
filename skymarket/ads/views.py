from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from ads.serializers import AdSerializer, AdListSerializer, CommentSerializer
from ads.models import Ad, Comment
from ads.permissions import IsOwner, IsAdmin



class AdPagination(pagination.PageNumberPagination):
    page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    default_serializer = AdSerializer
    serializer_classes = {
        "List": AdListSerializer,
    }
    default_permission = [AllowAny()]
    permissions = {

        "partial_update": [IsAuthenticated(), IsOwner()],
        "update": [IsAuthenticated(), IsOwner()],
        "delete": [IsAuthenticated(), IsOwner()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    http_method_names = ["get", "post", "patch", "delete"]

    def get_permissions(self):
        if self.action == "update":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(ad_id=self.kwargs.get("ad_id"), author_id=self.request.user.pk)

