from django.urls import path
from core import views
urlpatterns = [
    path('',views.home, name='home'),
    path('post/create_post/',views.create_post, name='create_post'),
    path('post/update_post/<int:post_id>/',views.update_post, name='update_post'),
    path('post/delete_post/<int:post_id>/',views.delete_post, name='delete_post')


]
