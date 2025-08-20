from django.contrib import admin

from .models import *

admin.site.register(Industry)
admin.site.register(Industry_Quarters)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(A_Performance)
admin.site.register(A_Revenue_Distribution)
admin.site.register(Q_Performance)

