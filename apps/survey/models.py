from django.db import models
from datetime import datetime
from apps.contest.models import ContestModel
from apps.users.models import ParticipantModel, JudgeModel


def survey_directory_path(instance, filename):
    today = datetime.now()
    return f"survey/survey_images/{today.year}/{today.month}/{today.day}/{filename}"


class SurveyModel(models.Model):
    participant = models.ForeignKey(ParticipantModel, on_delete=models.CASCADE)
    contest = models.ForeignKey(ContestModel, on_delete=models.CASCADE)
    user_comment = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=survey_directory_path)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'
        db_table = 'surv_surveys'


class ResultModel(models.Model):
    survey = models.OneToOneField(to=SurveyModel, on_delete=models.CASCADE)
    points = models.IntegerField()
    place = models.SmallIntegerField()
    judge = models.ForeignKey(JudgeModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.survey.name

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'
        db_table = 'surv_results'
