from django.contrib.auth.models import User
from stream.models import Stream, Lobby
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['title', 'thumbnail']


class LobbyForm(forms.ModelForm):
    class Meta:
        model = Lobby
        fields = ['lobbyname', 'logo', 'description']

    def __init__(self, *args, **kwargs):
        super(LobbyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'autocomplete': 'off',
            })
