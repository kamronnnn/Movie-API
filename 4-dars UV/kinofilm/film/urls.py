from django.urls import path
from .views import CategoryListView, MovieListView, CommentListView

urlpatterns = [
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/category/<int:pk>/', CategoryListView.as_view()),
    path('api/v1/movie/', MovieListView.as_view()),
    path('api/v1/movie/<int:pk>/', MovieListView.as_view()),
    path('api/v1/comment/', CommentListView.as_view()),
    path('api/v1/comment/<int:pk>/', CommentListView.as_view()),
]
