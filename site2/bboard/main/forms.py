from django import forms
from .models import AdvUser, Posts
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class RegisterUserForm(forms.ModelForm):
    fio = forms.CharField(label='Ваше ФИО', required=True, widget=forms.TextInput,
                          validators=[RegexValidator('([А-ЯЁ][а-яё]+[\-\s]?){3,}', message='ФИО введено не верно')])
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Повторите тот же самый пароль еще раз')
    send_messages = forms.BooleanField(label='Поставьте галочку', required=True)

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'fio', 'password1', 'password2',
                  'send_messages')


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой. Размер файла не должен превышать 2 МБ.')


class PostsForm(forms.ModelForm):
    image = forms.FileField(validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp']), file_size], label='Фотография',)
    class Meta:
        model = Posts
        fields = '__all__'
        widgets = {'author': forms.HiddenInput, 'status': forms.HiddenInput}


class FilterForm(forms.Form):
    CHOICES_STATUS = (
        ("о", 'Все'),
        ("Новый", 'Новый'),
        ("Принято в работу", 'Принято в работу'),
        ("Выполнено", 'Выполнено'),
    )
    keyword = forms.ChoiceField(choices=CHOICES_STATUS, label='Фильтр')

class SearchForm(forms.Form):
   keyword = forms.CharField(required=False, max_length=20, label='')