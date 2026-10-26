from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def inicio_sesion(request):
    if request.method == 'POST':
        # Procesa el formulario de login básico
        u = request.POST.get('username')
        p = request.POST.get('password')
        usuario = authenticate(request, username=u, password=p)
        if usuario is not None:
            login(request, usuario)
            return redirect('panel')
    return render(request, 'usuarios/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def panel(request):
    # Vista protegida
    return render(request, 'usuarios/panel.html', {'usuario': request.user})