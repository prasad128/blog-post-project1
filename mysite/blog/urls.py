from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('about',views.AboutView.as_view(),name='about'),
    path('create',views.PostCreateView.as_view(),name='create'),
    path('',views.PostListView.as_view(),name='list'),
    path('detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('delete/<int:pk>',views.PostDeleteView.as_view(),name='delete'),
    path('drafts',views.DraftListView.as_view(),name='postdraft'),
    path('update/<int:pk>',views.PostUpdateView.as_view(),name='update'),
    path('post/<int:pk>/comment',views.add_comment_to_post,name='comment'),
    path('comment/<int:pk>/approve',views.approveComment,name='approve'),
    path('comment/<int:pk>/remove',views.removeComment,name='remove'),
    path('post/<int:pk>/publish',views.publishPost,name='publish'),
]