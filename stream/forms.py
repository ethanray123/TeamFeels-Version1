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
        exclude = ('lobbies',)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        user = self.request.user
        super(StreamForm, self).__init__(*args, **kwargs)
        self.fields['owner']=forms.ModelChoiceField(
            queryset=Lobby.objects.filter(owner=user))
