from django.contrib import admin
from workout_helper.models import Workout
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Workout)
class ViewAdmin(ImportExportModelAdmin):
    pass
