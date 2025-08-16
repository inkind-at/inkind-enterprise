from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, help_text=_('Required.'))
    last_name = forms.CharField(max_length=150, required=True, help_text=_('Required.'))
    terms = forms.BooleanField(
        label=_("I accept the Terms and Conditions"),
        required=True,
    )
    privacy = forms.BooleanField(
        label=_("I acknowledge the Privacy Policy"),
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')
        help_texts = {
            'email': _('Changing your email will require re-verification.'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # The role is not editable by the user in their profile
        self.fields['email'].disabled = True
