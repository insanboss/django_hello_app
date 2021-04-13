from django.contrib.auth import login
from django.shortcuts import render, redirect


from accounts.forms import UserRegisterForm


def register_view(request, *args, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article:list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)