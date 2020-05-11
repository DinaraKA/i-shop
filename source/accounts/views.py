
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserCreationForm, UserInfoChangeForm, UserPasswordChangeForm
from main.settings import HOST_NAME
from accounts.models import Token, Profile
from django.http import HttpResponseRedirect




# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             user = User(
#                 username=form.cleaned_data['username'],
#                 # first_name=form.cleaned_data['first_name'],
#                 # last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email']
#             )
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             # Profile.objects.create(user=user)
#             login(request, user)
#             return redirect('webapp:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', context={'form': form})


def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                # phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                is_active=False  # user не активный до подтверждения email
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = Profile(
                user=user,
                mobile_phone=form.cleaned_data['phone_number'],
            )
            user.save()
            profile.save()
            # user.profile.mobile_phone = form.cleaned_data['phone_number']
            # user.profile.save()

            # токен для активации, его сложнее угадать, чем pk user-а.
            token = Token.objects.create(user=user)
            activation_url = HOST_NAME + reverse('accounts:user_activate') + '?token={}'.format(token)

            # отправка письма на email пользователя
            user.email_user('Регистрация на сайте localhost',
                            'Для активации перейдите по ссылке: {}'.format(activation_url))

            return redirect("webapp:index")
        else:
            return render(request, 'register.html', {'form': form})


def user_activate(request):
    token_value = request.GET.get('token')
    try:
        # найти токен
        token = Token.objects.get(token=token_value)

        # активировать пользователя
        user = token.user
        user.is_active = True
        user.save()

        # удалить токен, он больше не нужен
        token.delete()

        # войти
        login(request, user)

        # редирект на главную
        # return redirect('webapp:index')
        # return redirect('accounts:user_update')
        return HttpResponseRedirect(reverse('accounts:user_update', kwargs={"pk": user.pk}))
    except Token.DoesNotExist:
        # если токена нет - сразу редирект
        return redirect('webapp:index')


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_object'


class UserInfoChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_object'
    form_class = UserInfoChangeForm

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = UserPasswordChangeForm
    context_object_name = 'user_object'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:login')


