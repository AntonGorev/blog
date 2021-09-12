from .models import Orgpage
from django.shortcuts import render, get_object_or_404, redirect, reverse

from allauth.account.forms import LoginForm

def orgpage(request, slug):

    page = get_object_or_404(Orgpage, slug=slug)
    form_login = LoginForm()

    context = {
        'page': page,
        'form_login': form_login
    }
    return render(request, 'orgpage.html', context)