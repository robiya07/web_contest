from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ProfileForm
from django_email_verification import send_email
from .models import CustomUserModel, ParticipantModel, Organization


def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data['email']
            user_username = form.cleaned_data['username']
            user_password = form.cleaned_data['password1']
            organization = form.cleaned_data['inst']

            user = CustomUserModel.objects.create_user(username=user_username, email=user_email, password=user_password)
            ParticipantModel.objects.create(user=user, organization_type=organization)
            user.is_active = False
            send_email(user)

            return redirect('users:email-send')

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('users:profile')
    return render(request, 'login.html')


def email_send_view(request):
    return render(request, 'email_send.html')


def profile_view(request):
    if request.user.is_anonymous:
        return redirect('users:login')
    else:
        user = CustomUserModel.objects.get(username=request.user.username)
        user_p = ParticipantModel.objects.get(user=user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES)
                image = form.cleaned_data['image']
                gender = form.cleaned_data['gender']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                birth_date = form.cleaned_data['birth_date']
                address = form.cleaned_data['address']
                school = form.cleaned_data['school']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                current_password = form.cleaned_data['current_password']
                new_password = form.cleaned_data['new_password']
                confirm_password = form.cleaned_data['confirm_password']

                user_p.image = image
                user.gender = gender
                user.first_name = first_name
                user.last_name = last_name
                user.birth_date = birth_date
                user.username = username
                user.address = address

                if school:
                    user_p.organization = Organization.objects.get(id=school)
                user.phone = phone
                user.email = email

                if current_password and new_password and confirm_password:
                    if user.check_password(current_password) and new_password == confirm_password:
                        user.set_password(new_password)

                user.save()
                user_p.save()

    context = {
        'user': user,
        'user_p': user_p,
        'organizations': Organization.objects.filter(organization_type=user_p.organization_type)
    }

    return render(request, 'profile.html', context)
