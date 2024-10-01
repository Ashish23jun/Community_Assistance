from django.contrib import admin
from knowledge_hub.models import Query
#Register
admin.site.site_header = "Community Assistance"
admin.site.site_title = "Community Assistance Admin Portal"
admin.site.index_title = "Welcome to Community Assistance Portal"


admin.site.register(Query)