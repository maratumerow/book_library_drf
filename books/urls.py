from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()


urlpatterns = format_suffix_patterns(
    [
        path("create/", views.BookCreateViewSet.as_view({"post": "create"})),
        path("book/", views.BookViewSet.as_view({"get": "list"})),
        path(
            "book/<int:pk>/",
            views.BookViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        ),
    ]
)


router.register("genre", views.GenreViewSet)
router.register("author", views.AuthorViewSet)

urlpatterns += router.urls
