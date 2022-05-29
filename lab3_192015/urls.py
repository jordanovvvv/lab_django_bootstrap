
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('', views.PostDetail.as_view(), name='post_detail'),
    path('', views.comment, name='comment')
]
