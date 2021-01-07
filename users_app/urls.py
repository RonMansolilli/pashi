from django.urls import path
from .views import SignUpView

# from . import views

app_name = 'users_app'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

