from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('new/', views.new, name="new"),
    path('archive/', views.archive, name="archive"),
    re_path('detail/(?P<post_id>[0-9]+)/$', views.detail, name="detail"),
]
