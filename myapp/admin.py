from django.contrib import admin
from myapp.models import *

admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)