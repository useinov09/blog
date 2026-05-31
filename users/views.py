from django.shortcuts import render, redirect
from django.contrib.auth import login
from blogs.forms import CustomRegisterForm

def register(request):
    if request.method != 'POST':
        form = CustomRegisterForm()
    else:
        form = CustomRegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
