from django.urls import path

from apps.survey.views import survey_view, works_list_view

app_name = 'survey'

urlpatterns = [
    path('contest/<str:slug>/survey/', survey_view, name='survey'),
    path('works/', works_list_view, name='works_list'),
]
