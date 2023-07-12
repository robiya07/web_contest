from django.shortcuts import render

from apps.contest.models import ContestModel


def home_view(request):
    return render(request, 'main.html')


def contest_list_view(request):
    contests = ContestModel.objects.all()
    context = {
        "contests": contests
    }
    return render(request, 'competition.html', context)


def result_view(request):
    return render(request, 'result.html')


def works_list_view(request):
    return render(request, 'work.html')


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def contest_detail_view(request, slug):
    contest = ContestModel.objects.get(slug=slug)
    rules = contest.rulemodel_set.all()
    prizes = contest.prizemodel_set.all()
    context = {
        'contest': contest,
        'rules': rules,
        'prizes': prizes
    }
    return render(request, 'contest_detail.html', context)
