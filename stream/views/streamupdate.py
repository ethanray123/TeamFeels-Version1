from django.shortcuts import render, redirect
from django.views.generic import View
from stream.forms import StreamForm


class StreamFormView(View):
    form_class = StreamForm
    template_name = "stream/streamedit_form.html"

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # store data locally
            stream = form.save(commit=False)

            # save in database
            stream.save()

            # returns user objects if credentials are correct
            return redirect('stream:home')

        return render(request, self.template_name, {'form': form})
