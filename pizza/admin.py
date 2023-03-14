from django.contrib import admin
from .models import Pizza,Pizzacategory,Cart,Cart_items,faker_test,enqury

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Pizzacategory)
admin.site.register(Cart)
admin.site.register(Cart_items)
admin.site.register(faker_test)
admin.site.register(enqury)
