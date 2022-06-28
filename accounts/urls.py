from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/',views.login_page,name='login'),
    path('accounts/logout/',views.logout_page,name='logout'),
    path('accounts/register/',views.register_page,name='register'),
    path('accounts/edit/',views.profile_edit,name='edit'),
    path('accounts/users/',views.users_page,name='users'),
    path('accounts/favs/',views.my_favorite,name='fav'),
    path('accounts/fav/<str:pk>/',views.add_favorite,name='add-fav'),
    path('accounts/like/<str:pk>/',views.like_post,name='like'),
    path('accounts/follow/<str:pk>/',views.follow,name='follow'),
    path('accounts/<str:username>',views.profile,name='profile'),
]
