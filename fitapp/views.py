from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        return redirect('home')  
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

def history_view(request):
    return render(request, 'history.html')
