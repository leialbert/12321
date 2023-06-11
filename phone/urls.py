from django.urls import path
from .views import CheckPhoneNumberView

urlpatterns = [
    path('v1/check', CheckPhoneNumberView.as_view(), name='check-phone-number'),
]
