from django.urls import path
from .views import (
    PaymentView, 
    EnrollView, 
    CreateSubscriptionView, 
    RetryInvoiceView, 
    webhook, 
    ChangeSubscriptionView
)

app_name = "payment"

urlpatterns = [
    path('enroll/', EnrollView.as_view(), name='enroll'),
    path('enroll/<slug>/', PaymentView, name='payment'),
    path('create-subscription/', CreateSubscriptionView.as_view(), name='create-subscription'),
    path('change-subscription/', ChangeSubscriptionView.as_view(), name='change-subscription'),
    path('retry-invoice/', RetryInvoiceView.as_view(), name='retry-invoice'),
    path('webhook/', webhook, name='webhook')
]