from django.urls import path

from apps.contest.views import contest_list_view, home_view, result_view, works_list_view, contact_view, about_view, \
    contest_detail_view

app_name = 'contest'

urlpatterns = [
    path('', home_view, name='home'),
    path('contest/', contest_list_view, name='contest_list'),
    path('results/', result_view, name='results'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('contest/<str:slug>/', contest_detail_view, name='contest_detail'),
]
