from django.contrib import admin
from ecomm.models import Product,Cart,Ordered,Creator
# Register your models here.

admin.site.register(Creator)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Ordered)
