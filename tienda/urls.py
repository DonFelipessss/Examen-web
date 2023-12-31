from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from animalitos.views import InicioView, NosotrosView, TiendaView, ContactoView, DonacionesView,LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, ActivateView, LogOutView,ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView, RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView 
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    path('tienda/', TiendaView.as_view(), name='tienda'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('donaciones/', DonacionesView.as_view(), name='donaciones'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('activate/<code>/', ActivateView.as_view(), name='activate'),

    path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('change/email/', ChangeEmailView.as_view(), name='change_email'),
    path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
    
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)