from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import RequestContext
import pdb

def money_request(request):
    # pdb.set_trace()
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "item_name": "Event Registration",
        "notify_url": "http://20705043.ngrok.com" + reverse('paypal-ipn'),
        "return_url": "http://20705043.ngrok.com/paypal/confirm",
        "cancel_return": "http://20705043.ngrok.com/paypal/",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    # return render_to_response("paypal_rsa/payment.html", context, context_instance=RequestContext(request))
    return render_to_response("paypal_page.html", context, context_instance=RequestContext(request))

def show_me_the_money(sender, **kwargs):
    # pdb.set_trace()
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            Users.objects.update(paid=True)
    else:
        Users.objects.update(paid=False)

@csrf_exempt
def confirm(request):
    return render_to_response("paypal_rsa/confirm.html", context_instance=RequestContext(request))

valid_ipn_received.connect(show_me_the_money)
