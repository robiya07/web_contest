from django.shortcuts import render, redirect

from apps.contest.models import ContestModel
from apps.survey.forms import SurveyCreateForm
from apps.survey.models import ResultModel
from apps.users.models import ParticipantModel, CustomUserModel


# Create your views here.
def survey_view(request, slug):
    contest = ContestModel.objects.get(slug=slug)
    if request.method == 'POST':
        user = CustomUserModel.objects.get(id=request.user.id)
        participant = ParticipantModel.objects.get(user=user)
        form = SurveyCreateForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.contest = contest
            survey.participant = participant
            survey.save()
            return redirect('contest:contest_detail', slug=slug)

    context = {
        'contest': contest
    }
    return render(request, 'survey.html', context)


def works_list_view(request):
    print(1)
    works = ResultModel.objects.all()

    return render(request, 'work.html', {'works': works})