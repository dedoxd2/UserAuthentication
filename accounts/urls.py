from django.urls import path
from .import views
app_name = 'accounts'
urlpatterns = [
    path('signup', views.signup),

    path('profile', views.profile),
    path('profile/edit', views.edit_profile),
]
