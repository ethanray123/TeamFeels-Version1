import json

from django.shortcuts import get_object_or_404
from stream.models import Report, Streamer
from django.views.generic import View
from django.http import HttpResponse, Http404


class ReportView(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        reporter = get_object_or_404(Streamer, user=request.user)
        reportee = get_object_or_404(Streamer, pk=request.GET['streamer_id'])
        if(not reportee.is_reported(reporter) and
           reporter.user.username != reportee.user.username):
            Report.objects.create(
                reporter=reporter,
                violator=reportee)
            message = "Reported! Thanks!"
        else:
            if(reportee.is_reported(reporter)):
                message = "You have already reported this"
            else:
                message = "You can not report yourself"
        data = {
            'message': message}
        return HttpResponse(json.dumps(data), content_type="application/json")
