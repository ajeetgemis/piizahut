from django.apps import AppConfig


class PizzaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pizza'
    def ready(self):
        from django.contrib.auth.models import User
        def get_cart_count(self):
            from .models import Cart_items
            return Cart_items.objects.filter(cart__user=self,cart__is_paid=False).count()
        User.add_to_class("get_cart_count",get_cart_count)
    