from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-task/', views.create_task, name='create-task'),
    path('create-task/', views.create_task, name='create-task'),
    path('create-event/', views.create_event, name='create-event'),
    path('account/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('tasks/<int:pk>', views.task_detail, name='task-detail'),
    path('events/<int:pk>', views.event_detail, name='event-detail'),
    path('delete-event/<int:pk>', views.delete_event, name='delete-event'),
    path('update-event/<int:pk>', views.update_event, name='update-event'),
    path('delete-task/<int:pk>', views.delete_task, name='delete-task'),
    path('update-task/<int:pk>', views.update_task, name='update-task'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]