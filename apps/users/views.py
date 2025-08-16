from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegistrationForm, ProfileUpdateForm
from .models import CustomUser


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully! Please check your email to verify your account."

    def form_valid(self, form):
        # This is where you would add logic to send a verification email.
        # For now, we'll just save the user as inactive until they verify.
        user = form.save(commit=False)
        user.is_active = False # Set to False until email is verified
        user.save()
        # Send verification email logic here...
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    # Note: Account lockout is handled by django-axes middleware


class LogoutView(auth_views.LogoutView):
    # Redirects to LOGOUT_REDIRECT_URL from settings.py
    pass


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')
    success_message = "Your profile has been updated successfully."

    def get_object(self, queryset=None):
        return self.request.user
