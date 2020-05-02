from django.contrib.auth.mixins import UserPassesTestMixin
from webapp.models import Category
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render


class CategoryListView(UserPassesTestMixin, ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories'
    page_kwarg = 'page'

    def test_func(self):
        user = self.request.user
        return user.is_staff

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class CategoryCreateView(UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'add.html'
    fields = ['name']

    def test_func(self):
        user = self.request.user
        return user.is_staff

    def form_valid(self, form):
        text = form.cleaned_data['name']
        if Category.objects.filter(name=text.capitalize()):
            messages.error(self.request, 'Объект с таким названием уже существует!')
            return render(self.request, 'add.html', {})
        else:
            role = Category(name=text.capitalize())
            role.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:categories_list')


class CategoryUpdateView(UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'edit.html'
    fields = ['name']

    def test_func(self):
        user = self.request.user
        return user.is_staff or user.groups.filter(name='principal_staff')

    def form_valid(self, form):
        text = form.cleaned_data['name']
        if Category.objects.filter(name=text.capitalize()):
            print(text, 'tEXT')
            messages.error(self.request, 'Объект с таким названием уже существует!')
            return render(self.request, 'edit.html', {})
        else:
            pk = self.kwargs.get('pk')
            role = get_object_or_404(Category, id=pk)
            role.name = text.capitalize()
            role.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:categories_list')


class CategoryDeleteView(UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:categories_list')
    permission_required = "webapp.delete_category"
    permission_denied_message = "Доступ запрещен"

    def test_func(self):
        user = self.request.user
        return user.is_staff
