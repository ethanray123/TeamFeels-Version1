from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from stream.forms import UserForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from stream.models import Streamer


class UserFormView(View):
    form_class = UserForm
    template_name = "stream/registration_form.html"

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # store data locally
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # save in database
            user.save()

            newuser = get_object_or_404(User, username=username)
            Streamer.objects.create(user=newuser)
            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('stream:home')

        return render(request, self.template_name, {'form': form})
