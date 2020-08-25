from django.conf import settings
from django.http import JsonResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe

from djvideomem.content.models import Pricing

stripe.api_key = settings.STRIPE_SECRET_KEY


class EnrollView(generic.TemplateView):
    template_name = "payment/enroll.html"


class PaymentView(generic.TemplateView):
    template_name = "payment/checkout.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        pricing = get_object_or_404(Pricing, slug=kwargs["slug"])
        context.update({
            "pricing_tier": pricing,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateSubscriptionView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        customer_id = request.user.stripe_customer_id
        print(customer_id)
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': data["priceId"]}],
                expand=['latest_invoice.payment_intent'],
            )

            data = {}
            data.update(subscription)

            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })


class RetryInvoiceView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.stripe_customer_id
        try:

            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            invoice = stripe.Invoice.retrieve(
                data['invoiceId'],
                expand=['payment_intent'],
            )
            data = {}
            data.update(invoice)

            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })