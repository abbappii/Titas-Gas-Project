from django.urls import path
from AuthenticationApp import views as auth_view
from django.contrib.auth import views as core_auth_views

app_name = 'auth_app'
urlpatterns = [
    path('register/', auth_view.UserRegisterView, name='new_user_register'),
    path('user_verify/<uidb64>/', auth_view.UserVerification, name='user_verify'),
    path('login/', auth_view.LoginView, name='login'),
    path('opt_verify/<uuid>/', auth_view.OTP_Verification, name='otp_verification'),
    path('opt_resend/<hash>/', auth_view.OTP_Resend, name='otp_resend'),
    path('logout/', auth_view.LogOutView, name='log_out'),
    path('dashboard/', auth_view.profileDashboardView, name='profile_dashBoard'),
    path('pro_pic_update/', auth_view.profilePicUpdateView, name='profile_pic_update'),
    path('profile_update/', auth_view.profileUpdateView, name='profile_update'),
    # ***********profile update admin***********
    path('users_list/', auth_view.UserListTemplateView, name='user_list_template'),
    path('users_activation_list/', auth_view.UserActivationListTemplateView, name='user_activation_list_template'),
    path('api/users_list/', auth_view.UserListView.as_view(), name='user_list'),
    path('api/user_update/<id>/', auth_view.UpdateUserInfoAdminView.as_view(), name='user_update_api'),
    path('admin_update_profile/<user_id>/', auth_view.UserProfileUpdateAdminView, name='admin_update_profile'),

    #     password reset
    path("change_password/", auth_view.PasswordChangeView.as_view(), name="change_password"),
    path("change_password/done/", auth_view.PasswordChangeDoneView, name="password_change_done"),
    path("password_reset/", auth_view.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_view.PasswordResetDoneView, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView, name='password_reset_complete'),

    #  API list
    path('api/activation_request/', auth_view.AccountActivationListView.as_view(), name='activation_request_list'),
    path('api/activation_request/<id>/', auth_view.AccountActivationView.as_view(), name='user_activation'),
]
