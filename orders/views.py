from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from send_mail.views import send_new_order_email, send_new_order_email_with_template
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            email = form.cleaned_data.get("email")
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            request.session["order_id"] = order.id
            # Envoi un mail au client
            #send_mail(
            #    'Votre commande sur BebaShop',
            #    'Nous avons bien reçu votre commande.',
            #    'from@example.com',
            #    [email],
            #    fail_silently=False,
            #)
            #send_new_order_email(email)
            #send_new_order_email_with_template(email)
            return redirect("payment-process")
    else:
        form = OrderCreateForm()
    return render(request, "orders/create.html", {"cart": cart, "form": form})


def order_created(request):
    return render(request, "orders/created.html")
