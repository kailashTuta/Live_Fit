from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from ayurvedic_tips.models import AyurvedicTips
# Register your models here.


@admin.register(AyurvedicTips)
class ViewAdmin(ImportExportModelAdmin):
    pass
