from django.contrib import admin
from feedback_details.models import trainer_data, trainer_feedback
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.register(trainer_data)
admin.site.register(trainer_feedback)
class StudentResource(resources.ModelResource):

    class Meta:
        model = trainer_feedback
        import_id_fields = ('id',)
        # exclude = ('id', )
        # fields = ('id','text','option1','option2','option3','option4','answer','section')


class TrainerDataAdmin(ImportExportModelAdmin):
    # list_filter = ('department', 'team_no', 'score')
    # list_display = ('name', 'roll_no', 'score', 'team_no')


admin.site.register(trainer_feedback, TrainerDataAdmin)