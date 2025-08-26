from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

admin.site.register(Industry, ImportExportActionModelAdmin)
admin.site.register(Industry_Quarter, ImportExportActionModelAdmin)
admin.site.register(Company, ImportExportActionModelAdmin)
admin.site.register(Employee, ImportExportActionModelAdmin)
admin.site.register(Client, ImportExportActionModelAdmin)
admin.site.register(A_Performance, ImportExportActionModelAdmin)
admin.site.register(A_Revenue_Distribution, ImportExportActionModelAdmin)
admin.site.register(Q_Performance, ImportExportActionModelAdmin)

