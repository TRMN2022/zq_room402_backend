from django.urls import path, include, re_path

from api import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),

    # re_path(r'^user/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    # re_path(r'^user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    # re_path(r'^user/(?P<pk>\d+)/pwd_change/$', views.pwd_change, name='pwd_change'),
    # re_path(r"^logout/$", views.logout, name='logout'),

    path("users/records", views.RecordInfoView.as_view()),
    path("users/<int:pk>/records", views.UserRecordInfoView.as_view()),
    path("users/<int:pk1>/records/<int:pk2>", views.UserRecordInfoDetailView.as_view()),
    path("whereiskey", views.KeyInfoView.as_view()),
]
