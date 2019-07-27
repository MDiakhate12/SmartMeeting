from django.urls import path, include
from . import views
import notifications.urls

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('dashboard/create_meeting/', views.create_meeting, name='create_meeting'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/', views.meeting, name='meeting'),
    path('transcript/', views.transcript, name='transcript'),
    path('meeting/<int:id>', views.meeting, name='meeting'),
    path('stats/<int:id>', views.stats, name='stats'),
    path('calendar', views.calendar, name='calendar'),
    path('start_meeting/<int:id>', views.start_meeting, name='start_meeting'),
    path('go_to_meeting/<int:id>', views.go_to_meeting, name='go_to_meeting'),
    path('confirm_invitation/', views.confirm_invitation, name='confirm_invitation'),
    path('messages/<int:id>', views.join_all, name='messages'),
    path('resume/<int:id>', views.resume, name='resume'),
    path('pv/<int:id>', views.pv, name='pv'),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
] 