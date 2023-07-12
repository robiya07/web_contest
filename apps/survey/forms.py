from django import forms

from apps.survey.models import SurveyModel


class SurveyCreateForm(forms.ModelForm):
    class Meta:
        model = SurveyModel
        fields = ('file', 'name', 'user_comment')
