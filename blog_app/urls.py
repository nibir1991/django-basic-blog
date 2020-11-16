"""MyBLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import HomeView,PostView,AddPost,UpdatePost,DeletePost,AddCategory,CategoryView,LikeView,AddComment

urlpatterns = [
    
    path('', HomeView.as_view() ,name='home'),
    path('post/<int:pk>',PostView.as_view(),name='post'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path('post/update/<int:pk>', UpdatePost.as_view(),name='update_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(),name='delete_post'),
    path('add_category/', AddCategory.as_view(),name='add_category'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/comment',AddComment.as_view(),name='add_comment'),
]
