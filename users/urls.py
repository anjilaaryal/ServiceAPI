from django.urls import path, include
from users.views import UserSignUpView, UserLoginView

urlpatterns = [
    path('', UserSignUpView.as_view()),
    path('login/', UserLoginView.as_view()),

]