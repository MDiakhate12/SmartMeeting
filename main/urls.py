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
    path('calendar', views.calendar, name='calendar'),
    path('start_meeting/<int:id>', views.start_meeting, name='start_meeting'),
    path('confirm_invitation/', views.confirm_invitation, name='confirm_invitation'),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
] 