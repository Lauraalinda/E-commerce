
from django.contrib import admin

from product.models import Categories,Product,Cart,CartItem

# Register your models here.
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)