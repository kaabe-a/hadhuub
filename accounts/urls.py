from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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

    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),name='change_password'),
	path('accounts/password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),


	path('accounts/reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),name='reset_password'),
	path('accounts/reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
	path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
	path('accounts/reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),

]
