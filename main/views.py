from django.shortcuts import render, redirect
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required
# from invitations.models import Invitation
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User  # , AnonymousUser
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

from django.db.models.signals import post_save
from notifications.signals import notify
from .summerize import summerize
from .similarity import *


def index(request):
    return render(request, 'main/index.html')


def create_meeting(request):
    users = User.objects.all()
    meetings = request.user.meetings.all()

    if request.method == 'POST':
        meetingForm = MeetingForm(request.POST)
        if meetingForm.is_valid():
            meeting = meetingForm.save()
            if (not request.user in meeting.members.all()):
                meeting.members.add(request.user)
            meeting.save()
            if(meeting.previous_meeting):
                previous_meeting = Meeting.objects.get(
                    pk=meeting.previous_meeting.id)
                previous_meeting.next_meeting = meeting
                previous_meeting.save()

            if(meeting.next_meeting):
                next_meeting = Meeting.objects.get(pk=meeting.next_meeting.id)
                next_meeting.previous_meeting = meeting
                next_meeting.save()
    else:
        meetingForm = MeetingForm()

    context = {'meetingForm': meetingForm, 'users': users, 'meetings': meetings,
               'page_title': 'DASHBOARD', 'messages': messages.get_messages(request)}

    return render(request, 'main/dashboard_meeting.html', context)


def send_confirmation_mail(request, emails=[]):

    users = User.objects.all()
    user = request.user

    html_message = render_to_string(
        'main/mail_invitation.html')

    print('---------------------------------------------------------------------------')
    print('request - mail', request)
    print('---------------------------------------------------------------------------')

    send_mail(
        subject='Invitation SmartMeeting',
        message=strip_tags(html_message),
        from_email='mdiakhate1297@gmail.com',
        recipient_list=[
            email for email in emails if email != request.user.email],
        html_message=html_message
    )


@login_required(redirect_field_name='login')
def dashboard(request):
    users = User.objects.all()

    meetings = request.user.meetings.all()
    meetingForm = MeetingForm()

    if(request.method == 'POST'):
        emails = [request.POST['email'+str(i)]
                  for i in range(len(request.POST)-1)]
        print('----------------------------------')
        print('request - dashboard', request.POST)
        print('----------------------------------')
        send_confirmation_mail(request, emails)
        messages.success(request, 'Invites are successfully sent !')

    not_started_meetings = request.user.meetings.filter(
        done=False, doing=False)

    context = {'meetingForm': meetingForm, 'users': users, 'meetings': meetings,
               'page_title': 'DASHBOARD', 'messages': messages.get_messages(request), 'not_started_meetings': not_started_meetings}

    return render(request, 'main/dashboard.html', context)


@login_required(redirect_field_name='login')
def meeting(request, id=False):
    if(id):
        meeting = Meeting.objects.get(pk=id)
        return render(request, 'main/dashboard_meeting_detail.html', {'meeting': meeting, 'page_title': meeting.title})
    meetings = request.user.meetings.all()
    return render(request, 'main/dashboard_meeting.html', {'meetings': meetings, 'page_title': 'MEETINGS'})


def calendar(request):
    return render(request, 'main/calendar.html', {'page_title': 'CALENDAR'})


@login_required(redirect_field_name='login')
def profile(request, id=False):
    if(id):
        user = User.objects.get(pk=id)
        return render(request, 'main/profile.html', {'user_profile': user})
    return render(request, 'main/profile.html')


def transcript(request):
    return render(request, 'main/transcript.html', {'page_title': 'LIVE MEETING TRANSCRIPTION'})


def start_meeting(request, id):
    meeting = Meeting.objects.get(pk=id)
    chat = ChatRoom(eid=meeting.id)
    chat.save()

    meeting.begin = timezone.now()
    meeting.doing = True

    meeting.chatroom = chat
    meeting.save()
    # send notification

    sender = request.user
    receivers = meeting.members.exclude(pk=sender.id)
    verb = "New meeting invitation"
    url = request.get_host() + '/' + str(meeting.id)
    description = "new live meeting " + '<a href ="http://' + url + '">here</a>'

    for receiver in receivers:
        # , action_object=, target=, description=, public=, timestamp=)
        notification = {
            'sender': sender,
            'recipient': receiver,
            'verb': verb,
            'description': description,
            'level': 'info',
            # 'action_object': receiver.notifications,
            # 'target': receiver.notifications,
            # 'description': '',
            # 'public': '',
            # 'timestamp': ''
        }

        notify.send(**notification)

        print('-----------------------------------------------------------')
        print(receiver.notifications.all())
        print('-----------------------------------------------------------')

    return redirect('room', room_id=meeting.id)


def go_to_meeting(request):
    pass


def confirm_invitation(request):
    users = User.objects.all()
    user = request.user

    if user in users:
        if user.is_authenticated:
            return redirect('dashboard')
        return redirect('login')
    return redirect('register')


def resume(request):
    pass


def join_all(request, id):
    meeting = Meeting.objects.get(pk=id)

    topics = meeting.points

    interventions = []

    for user in meeting.members.all():
        messages = user.messages.all()

        interventions.append({
            'user': user,
            'messages': messages
        })

    return render(request, 'main/messages.html', {'meeting': meeting, 'interventions': interventions})


def resume(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, 'main/resume.html', {'meeting': meeting})

def pv(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, 'main/pv.html', {'meeting': meeting})


def stats(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, 'main/stats.html', {'meeting': meeting})