from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import CustomUser


class CustomRegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        google_login_url = reverse_lazy("social:begin", args=["google-oauth2"])
        return render(request, "register.html", {"google_login_url": google_login_url})

    def post(self, request):
        phone_number = request.POST.get("phone_number", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        if not phone_number or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("register")

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return redirect("register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number is already registered.")
            return redirect("register")

        user = CustomUser.objects.create_user(phone_number=phone_number, email=email, password=password)
        login(request, user)  # Auto-login after registration
        messages.success(request, "Registration successful! You are now logged in.")
        return redirect("home")

class CustomLoginView(View):
    def get(self, request):
        google_login_url = reverse_lazy("social:begin", args=["google-oauth2"])
        return render(request, "login.html", {"google_login_url": google_login_url})

    def post(self, request):
        identifier = request.POST.get("identifier", "").strip()  # Can be email or phone number
        password = request.POST.get("password", "").strip()

        if not identifier or not password:
            messages.error(request, "Email/Phone and password are required.")
            return redirect("login")

        user = None
        if "@" in identifier:
            try:
                user = CustomUser.objects.get(email=identifier)
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect("login")
        else:  # Otherwise, treat it as a phone number
            try:
                user = CustomUser.objects.get(phone_number=identifier)
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid phone number or password.")
                return redirect("login")

        user = authenticate(request, phone_number=user.phone_number, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("login")


def home_view(request):
    return render(request, "home.html")


# Google OAuth Login
def oauth_login_view(request):
    try:
        return redirect(reverse("social:begin", args=["google-oauth2"]))
    except Exception as e:
        messages.error(request, f"OAuth Error: {str(e)}")
        return redirect("login")
