from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('dashboard')  # Change 'dashboard' to the name of your dashboard URL pattern
        else:
            # Return an error message or render the login page again with an error message
            return render(request, 'management/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'management/login.html')