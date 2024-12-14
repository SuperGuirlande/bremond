from django.contrib import admin
from .models import JobAnnonce


@admin.register(JobAnnonce)
class JobAnnonceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'last_updated')