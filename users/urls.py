# Done by Carlos Amaral (2020/10/27)

from django.urls import path

from .views import SignUpView

urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
]
