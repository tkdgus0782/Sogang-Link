# urls.py
from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView


urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comments', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
]