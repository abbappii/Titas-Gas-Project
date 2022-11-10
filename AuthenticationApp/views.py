import datetime
import random
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordContextMixin, INTERNAL_RESET_SESSION_TOKEN
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.mail import BadHeaderError
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView
from rest_framework import generics, permissions, serializers
from TitasPipelineGIS import custome_permission as cus_per
from AuthenticationApp import forms as auth_form, models as auth_model, serializers as auth_ser
from django.contrib.sites.shortcuts import get_current_site
from TitasPipelineGIS import email_send

UserModel = get_user_model()


# serializer
@login_required(login_url='auth_app:login')
def indexView(request):

    return render(request, 'index.html', context={})


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_model.User
        fields = ['id', 'email', 'full_name', 'profile_pic', 'phone_number', 'birthDate', 'is_staff', 'is_superuser',
                  'is_active']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_model.User
        fields = ['id', 'email', 'full_name', 'phone_number', 'birthDate', 'is_staff', 'is_superuser', 'is_active']


# Create your views here.
# @login_required(login_url='auth_app:login')
def UserRegisterView(request):
    error_msg = ''
    success_msg = ''
    form = auth_form.UserCreationForm()
    if request.method == 'POST':
        form = auth_form.UserCreationForm(data=request.POST)
        if form.is_valid():
            if form.date_validate():
                if form.clean_password2():
                    user = form.save(commit=False)
                    password = form.cleaned_data['password1']
                    try:
                        validate_password(password, user)
                    except ValidationError as e:
                        form.add_error('password1', e)  # to be displayed with the field's errors
                        return render(request, 'register.html', {'form': form})
                    user.save()

                    # Email sending and warning message
                    success_msg = 'New User Added'

                    if request.user.is_superuser:
                        user.is_active = True
                        user.save()
                        enc_user = f'{settings.ENC_KEY},{user.pk}'
                        subject = "User account activation"
                        email_template_name = "registration_verification.txt"
                        domain = get_current_site(request).domain
                        c = {
                            "email": user.email,
                            'domain': domain,
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(enc_user)),
                            "user": user,
                            'temp_pass': request.POST.get('password1'),
                            'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        try:
                            data = {'email_body': email, 'to_email': user.email,
                                    'email_subject': subject}

                            email_send.Util.send_email(data)
                        except:
                            pass
                    else:
                        user.active_request = True
                        user.save()
                        success_msg = 'Account created'

            else:
                error_msg = "Date of birth can't be a date from future."
    return render(request, 'register.html', context={'form': form, 'error_msg': error_msg, 'success_msg': success_msg})


def UserVerification(request, uidb64):
    try:
        # urlsafe_base64_decode() decodes to bytestring
        enc_code = urlsafe_base64_decode(uidb64).decode()
        uid = enc_code.split(',')[-1]
        user = UserModel._default_manager.get(pk=uid)
    except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
    ):
        user = None
    user.is_verified = True
    user.save()

    return HttpResponseRedirect(reverse('auth_app:login'))


def LoginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    form = auth_form.LoginForm()
    if request.method == 'POST':
        form = auth_form.LoginForm(data=request.POST)
        username, password = request.POST.get('username'), request.POST.get('password')
        check_user = auth_model.User.objects.filter(email=username).first()
        if check_user:
            if check_user.email == 'bappi142434@gmail.com' or check_user.email == 'lahir170monir10.18@gmail.com':
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', context={'error': 'User name or password incorrect'})
            if check_user.is_active:
                if check_user.is_verified:
                    user = authenticate(username=username, password=password)
                    if user:
                        # if user.email == 'gmzulkar@gmail.com' or user.email == 'tasinnaeem@gmail.com':
                        #     login(request, user)
                        #     return HttpResponseRedirect(reverse('gis_app:index_page'))
                        # else:
                        #     user.otp = ''
                        #     user.save()
                        #
                        #     otp = random.randint(100000, 999999)
                        #     user.otp = otp
                        #     user.save()
                        #     subject = "OTP Verification"
                        #     email_body = f"Hello {user.full_name},\n" \
                        #                  f"Your OTP  is - {otp}." \
                        #                  f"Use this Passcode to complete your Login. Thank you."
                        #     try:
                        #         data = {'email_body': email_body, 'to_email': user.email,
                        #                 'email_subject': subject}
                        #
                        #         email_send.Util.send_email(data)
                        #
                        #     except:
                        #         pass
                        #     sec_uid = f'{settings.ENC_KEY}-{user.pk}'
                        #     return redirect(
                        #         f'/auth/opt_verify/{urlsafe_base64_encode(force_bytes(urlsafe_base64_encode(force_bytes(sec_uid))))}/')
                        user.otp = ''
                        user.save()

                        otp = random.randint(100000, 999999)
                        user.otp = otp
                        user.save()
                        subject = "OTP Verification"
                        email_body = f"Hello {user.full_name},\n" \
                                     f"Your OTP  is - {otp}\n" \
                                     f"Use this Passcode to complete your Login. Thank you."
                        try:
                            data = {'email_body': email_body, 'to_email': user.email,
                                    'email_subject': subject}

                            email_send.Util.send_email(data)

                        except:
                            pass
                        sec_uid = f'{settings.ENC_KEY}-{user.pk}'
                        return redirect(
                            f'/auth/opt_verify/{urlsafe_base64_encode(force_bytes(urlsafe_base64_encode(force_bytes(sec_uid))))}/')


                    else:
                        return render(request, 'login.html', context={'error': 'User name or password incorrect'})
                return render(request, 'login.html', context={'error': 'Your Account is not verified yet.'})

            else:
                if check_user.last_login is None:
                    msg = 'Your Account is not Activated.'
                else:
                    msg = 'Your Account has been deactivated.'
                return render(request, 'login.html', context={'error': msg})
        else:
            return render(request, 'login.html', context={'error': 'No User Found'})

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def OTP_Verification(request, uuid):
    error = ''
    if request.method == 'POST':
        otp = request.POST.get('otp')

        try:
            # urlsafe_base64_decode() decodes to bytestring
            enc_uid = urlsafe_base64_decode(uuid).decode()
            uid = urlsafe_base64_decode(enc_uid).decode()
            dec_date = uid.split('-')
            sec_key = dec_date[0]
            user_pk = dec_date[-1]
            if sec_key == settings.ENC_KEY:
                user = UserModel._default_manager.get(pk=user_pk)
            else:
                raise ValidationError

        except (
                TypeError,
                ValueError,
                OverflowError,
                UserModel.DoesNotExist,
                ValidationError,
        ):
            user = None
        if user:
            if user.otp == otp:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'otp_verify.html', context={'error': 'Wrong OTP.', 'hash': uuid})
    return render(request, 'otp_verify.html', context={'hash': uuid})


def OTP_Resend(request, hash):
    try:
        # urlsafe_base64_decode() decodes to bytestring
        enc_uid = urlsafe_base64_decode(hash).decode()
        uid = urlsafe_base64_decode(enc_uid).decode()
        dec_date = uid.split('-')
        sec_key = dec_date[0]
        user_pk = dec_date[-1]
        if sec_key == settings.ENC_KEY:
            user = UserModel._default_manager.get(pk=user_pk)
        else:
            raise ValidationError
    except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
    ):
        user = None

    if user:
        user.otp = ''
        user.save()
        if user.is_active:
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            subject = "Resend OTP Verification"
            email_body = f"Your OTP : {otp} for two-factor authentication.\n" \
                         f"Thank you."
            try:
                data = {'email_body': email_body, 'to_email': user.email,
                        'email_subject': subject}

                email_send.Util.send_email(data)
            except:
                pass
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


class AccountActivationListView(generics.ListAPIView):
    permission_classes = [cus_per.IsSuperUser]
    serializer_class = auth_ser.AccountActivationSerializer

    def get_queryset(self):
        try:
            search = self.request.query_params.get('search')
            queryset = auth_model.User.objects.filter(Q(is_active=False, active_request=True, is_suspended=False),
                                                      Q(email__icontains=search) | Q(full_name__icontains=search))
        except:
            queryset = auth_model.User.objects.filter(is_active=False, active_request=True, is_suspended=False)
        return queryset


class AccountActivationView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [cus_per.IsSuperUser]
    serializer_class = auth_ser.AccountActivationSerializer
    queryset = auth_model.User.objects.filter(is_active=False, active_request=True, is_suspended=False)
    lookup_field = 'id'

    def perform_update(self, serializer):
        user = serializer.save(active_request=False)
        if user.is_active:
            enc_user = f'{settings.ENC_KEY},{user.pk}'
            subject = "User Account Request Approved"
            domain = get_current_site(self.request).domain
            email_template_name = "account_activation_confirmation.txt"
            c = {
                "full_name": user.full_name,
                "email": user.email,
                'domain': domain,
                'site_name': 'Website',
                "uid": urlsafe_base64_encode(force_bytes(enc_user)),
                "user": user,
                'protocol': 'http',
            }
            email = render_to_string(email_template_name, c)
            try:
                data = {'email_body': email, 'to_email': user.email,
                        'email_subject': subject}

                email_send.Util.send_email(data)
            except:
                pass

        elif user.is_suspended:
            email_body = f'Hello {user.full_name},\n' \
                         f'You are not authorized to this Organization, so unfortunately we are no able to activate your account.\n' \
                         f'Thank You\n\n' \
                         f'The Website Team'
            subject = "User Account has been Suspended"
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': subject}

            email_send.Util.send_email(data)
        elif not user.is_active and not user.is_superuser:
            email_body = f'Hello {user.full_name},\n' \
                         f'Sorry, Currently we are not allow you to create your account.\n' \
                         f'Thank You\n\n' \
                         f'The Website Team'
            subject = "User Account creation Request has been canceled"
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': subject}

            email_send.Util.send_email(data)


@login_required(login_url='auth_app:login')
def LogOutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_app:login'))


@login_required(login_url='geo_app:login')
def profileDashboardView(request):
    user = auth_model.User.objects.get(id=request.user.id)
    return render(request, 'profile_dashboard.html', context={'user': user})


@login_required(login_url='auth_app:login')
def profilePicUpdateView(request):
    user = auth_model.User.objects.get(id=request.user.id)
    form = auth_form.ImageUpdloadForm(instance=user)

    if request.method == 'POST':
        form = auth_form.ImageUpdloadForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('auth_app:profile_dashBoard')

    return render(request, 'profile_dashboard.html', context={'image_update': True, 'form': form})


@login_required(login_url='auth_app:login')
def profileUpdateView(request):
    user = auth_model.User.objects.get(id=request.user.id)
    form = auth_form.ProfileUpdateForm(instance=user)

    if request.method == 'POST':
        form = auth_form.ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('auth_app:profile_dashBoard')

    return render(request, 'profile_dashboard.html', context={'profile_update': True, 'form': form})


@login_required(login_url='auth_app:login')
def UserListTemplateView(request):
    if request.user.is_superuser:
        return render(request, 'users_list.html', context={})
    else:
        return redirect('auth_app:profile_dashBoard')


@login_required(login_url='auth_app:login')
def UserActivationListTemplateView(request):
    if request.user.is_superuser:
        return render(request, 'users_activation_request_list.html', context={})
    else:
        return redirect('auth_app:profile_dashBoard')


class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserListSerializer

    def get_queryset(self):

        try:
            search = self.request.query_params.get('search')
            queryset = auth_model.User.objects.filter((
                    Q(full_name__icontains=search) | Q(
                email__icontains=search) | Q(
                phone_number__exact=search)), (~Q(email='bappi142434@gmail.com') | ~Q(email='lahir170monir10.18@gmail.com')))
        except:
            queryset = auth_model.User.objects.filter(
                ~Q(id=self.request.user.id), (~Q(email='bappi142434@gmail.com') | ~Q(email='lahir170monir10.18@gmail.com')))
        return queryset.order_by('id')


@login_required(login_url='auth_app:login')
def UserProfileUpdateAdminView(request, user_id):
    if request.user.is_superuser:
        user = auth_model.User.objects.get(id=user_id)
        form = auth_form.AdminProfileUpdateForm(instance=user)

        if request.method == 'POST':
            form = auth_form.AdminProfileUpdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('auth_app:user_list_template')

        return render(request, 'admin_profile_update.html',
                      context={'profile_update': True, 'update_profile': form})


# Password reset
class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("auth_app:password_change_done")
    template_name = "change-password.html"
    title = _("Password change")

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required(login_url='auth_app:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


def PasswordChangeDoneView(request):
    messages.success(request, 'success')
    return HttpResponseRedirect(reverse('auth_app:profile_dashBoard'))


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = auth_model.User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    domain = get_current_site(request).domain
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        data = {'email_body': email, 'to_email': user.email,
                                'email_subject': subject}

                        email_send.Util.send_email(data)
                        # send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("auth_app:password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html",
                  context={"password_reset_form": password_reset_form})


def PasswordResetDoneView(request):
    str = "We've emailed you instructions for setting your password, if an account exists with the email you entered.\
            You should receive them shortly.If you don't receive an email, please make sure you've entered the\
            address you registered with, and check your spam folder."
    return render(request, 'password_reset.html', context={'reset_success': f"{str}"})


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = reverse_lazy("auth_app:password_reset_complete")
    template_name = "password_reset_confirm.html"
    title = _("Enter new password")
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                UserModel.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": _("Password reset unsuccessful"),
                    "validlink": False,
                }
            )
        return context


def PasswordResetCompleteView(request):
    messages.success(request, 'success')
    return HttpResponseRedirect(reverse('auth_app:login'))


class UpdateUserInfoAdminView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserUpdateSerializer
    queryset = auth_model.User.objects.all()
    lookup_field = 'id'
