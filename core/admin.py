from django.contrib import admin

from core.models import Product, Variants, OptionTypes, OptionValues

admin.site.register(Product)
admin.site.register(OptionTypes)
admin.site.register(OptionValues)
admin.site.register(Variants)
