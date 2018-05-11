from django.shortcuts import get_object_or_404, render
from stream.models import Report, Streamer, Lobby


def report(request, streamer_id, lobby_id):
    reporter = get_object_or_404(Streamer, user=request.user)
    reportee = get_object_or_404(Streamer, pk=streamer_id)
    lobby = get_object_or_404(Lobby, pk=lobby_id)
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
    return render(
        request, 'stream/lobby.html',
        {
            'lobby': lobby,
            'message': message,
        }
    )
