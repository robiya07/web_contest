from django.contrib import admin

from apps.survey.models import ResultModel, SurveyModel

# Register your models here.
admin.site.register(ResultModel)
admin.site.register(SurveyModel)