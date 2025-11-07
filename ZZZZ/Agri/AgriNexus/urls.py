from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("payment/", views.payment, name="payment"),
    path("cart/", views.cart, name="cart"),
    path("Account/", views.Account, name="Account"),
    path("pesticides/", views.pesticides, name="pesticides"),
    path("gromart/", views.gromart, name="gromart"),
    path("fruits/", views.fruits, name="fruits"),
    path("vegetables/", views.vegetables, name="vegetables"),
    path("grains/", views.grains, name="grains"),
    path("Order/", views.Order, name="Order"),
    path("vegetables/", views.vegetables, name="vegetables"),
]
