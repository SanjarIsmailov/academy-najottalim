from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        if not phone_number or not password:
            return render(request, 'login.html', {'error': 'Phone number and password are required'})

        user = authenticate(request, phone_number=phone_number, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid phone number or password'})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to login page after logout

def home_view(request):
    return render(request, 'home.html')