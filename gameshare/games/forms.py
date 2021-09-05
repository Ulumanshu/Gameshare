from django import forms
from .models import Games, Items
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = (
            'name',
            'game_id',
            'owner_id',
            'rentee_id',
            'status',
            'rent_price',
            'date_rent_start',
            'date_rent_end'
        )

    def is_valid(self):
        return super(ItemForm, self).is_valid()


class GameForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ('name', 'photo', 'author', 'description', 'pub_date', 'label')

    def is_valid(self):
        return super(GameForm, self).is_valid()

    # def clean_name(self):
    #     text = self.cleaned_data.get('text')
    #     badwords = ['fuck', 'kaka', 'audi']
    #     check_list = [True if w in text else False for w in badwords]
    #     # if title exists create slug from title
    #     if True in check_list:
    #         for word in badwords:
    #             text = text.replace(word, '*' * len(word))

    # return text

class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label='User Name')
    password1 = forms.CharField(max_length=20, help_text=True, widget=forms.PasswordInput,
                                label='Password', error_messages={'required': 'field is required '})
    password2 = forms.CharField(max_length=20, help_text=True, widget=forms.PasswordInput,
                                label='Confirm password', error_messages={'required': 'field is required '})

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]