from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login/')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/already-logged-in.html', {})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password'}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        # return redirect('/')
        next = request.GET.get('next', None)
        if next:
            return redirect(next)
        else:
            return redirect('/')

    return render(request, 'accounts/login.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login/')
    return render(request, 'accounts/logout.html', {})
