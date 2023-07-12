from django.contrib import admin

from apps.users.models import ParticipantModel, CustomUserModel, JudgeModel, Organization

# Register your models here.
admin.site.register(ParticipantModel)
admin.site.register(JudgeModel)
admin.site.register(CustomUserModel)
admin.site.register(Organization)
