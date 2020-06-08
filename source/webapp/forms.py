from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, inlineformset_factory
from webapp.models import OrderProduct, Order, Product, Image


class CartOrderCreateForm(ModelForm):
    def __init__(self, user=None, **kwargs):
        self.user = user
        if user and not user.is_authenticated:
            self.user = None
        super().__init__(**kwargs)

    def clean_first_name(self):
        if not self.user and not self.cleaned_data.get('first_name'):
            raise ValidationError('Вы должны авторизоваться либо указать ваше имя!')

    def clean_email(self):
        if not self.user and not self.cleaned_data.get('email'):
            raise ValidationError('Вы должны авторизоваться либо указать ваш email!')

    def clean_phone(self):
        if not self.user and not self.cleaned_data.get('phone'):
            raise ValidationError('Вы должны авторизоваться либо указать ваш телефон!')

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone']


class ManualOrderForm(ModelForm):
    def clean_first_name(self):
        if not self.user and not self.cleaned_data.get('first_name'):
            raise ValidationError('Вы должны указать пользователя либо его имя!')

    def clean_email(self):
        if not self.user and not self.cleaned_data.get('email'):
            raise ValidationError('Вы должны указать пользователя либо его email!')

    def clean_phone(self):
        if not self.user and not self.cleaned_data.get('phone'):
            raise ValidationError('Вы должны указать пользователя либо его телефон!')

    class Meta:
        model = Order
        fields = ['user', 'first_name', 'last_name', 'email', 'address', 'phone']


class OrderProductForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product', 'amount']

class ProductForm(forms.ModelForm):
    tags = forms.CharField(max_length=101, required=False, label='Тэги')

    class Meta:
        model = Product
        exclude = ['in_stock', 'date', 'tags']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', '')
        tags = tags.split(',')
        tags = [tag.strip() for tag in tags]
        tags = filter(lambda tag: len(tag) > 0, tags)
        return tags

ImageFormset = inlineformset_factory(Product, Image, fields='__all__', extra=1, validate_min=False, min_num=0, can_delete=True)


ProductsFormset = inlineformset_factory(Order, OrderProduct, OrderProductForm, extra=0,
                                        validate_min=True, min_num=1, can_delete=True)