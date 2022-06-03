from django.urls import path
from .views import payment_process, payment_done, payment_cancelled


urlpatterns = [
    path("payment-process/", payment_process, name="payment-process"),
    path("payment-done/", payment_done, name="payment-done"),
    path("payment-cancelled/", payment_cancelled, name="payment-cancelled")
]
