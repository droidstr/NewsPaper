from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UserForm
# Create your views here.


class UserEdit(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_edit.html'
    context_object_name = 'post'
    success_url = reverse_lazy('news')


@login_required
def become_an_author(request):
    user = request.user
    premium_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        premium_group.user_set.add(user)
    return redirect('/news/')