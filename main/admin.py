from django.contrib import admin

from main.models import Plans,UserSubscription,Device


admin.site.register(UserSubscription)
admin.site.register(Plans)
admin.site.register(Device)



