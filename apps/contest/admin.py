from django.contrib import admin

from apps.contest.models import ContestModel, RuleModel, PrizeModel

admin.site.register(ContestModel)
admin.site.register(RuleModel)
admin.site.register(PrizeModel)
