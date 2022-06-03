from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from paydunya import InvoiceItem, Store, Invoice
from django.conf import settings
from orders.models import Order
import paydunya

from send_mail.views import payment_successful_email

paydunya.debug = True

paydunya.api_keys = settings.PAYDUNYA_ACCESS_TOKENS

store = Store(name="Boutique chez Beba")


def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, pk=order_id)
    order_items = order.items.all()
    items = [InvoiceItem(
        name=item.product.name,
        quantity=item.quantity,
        unit_price=str(item.price),
        total_price=str(item.price * item.quantity),
        description=item.product.name
    ) for item in order_items]
    invoice = paydunya.Invoice(store)
    #host = request.get_host
    #print('Response Host', host)
    invoice.callback_url = f"http://localhost:8000/payment-done"
    invoice.cancel_url = f"http://localhost:8000/payment-cancelled"
    # invoice.return_url = f"http://{host}/payment-cancelled"
    invoice.add_items(items)
    successful, response = invoice.create()
    if successful:
        return redirect(response.get("response_text"))


def payment_done(request):
    token = request.GET.get("token")
    invoice = Invoice(store)
    successful, response = invoice.confirm(token)
    if successful:
        return HttpResponse("<h2>Merci pour le payement </h2>")


def payment_cancelled(request):
    return HttpResponse("<h2>Vous avez annulé le paiement</h2>")
