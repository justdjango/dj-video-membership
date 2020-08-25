from django.urls import path
from .views import PaymentView, EnrollView, CreateSubscriptionView, RetryInvoiceView

app_name = "payment"

urlpatterns = [
    path('enroll/', EnrollView.as_view(), name='enroll'),
    path('enroll/<slug>/', PaymentView.as_view(), name='payment'),
    path('create-subscription/', CreateSubscriptionView.as_view(), name='create-subscription'),
    path('retry-invoice/', RetryInvoiceView.as_view(), name='retry-invoice')
]