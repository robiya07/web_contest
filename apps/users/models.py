from django.db import models
from django.contrib.auth.models import AbstractUser


def participant_directory_path(instance, filename):
    return "user/participant_image/user_{0}".format(instance.id)


def judge_directory_path(instance, filename):
    return "user/judge_image/user_{0}".format(instance.id)


class CustomUserModel(AbstractUser):
    class GENDER(models.TextChoices):
        MALE = "male", "Мужской"
        FEMALE = "female", "Женский"

    phone = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER.choices, default=GENDER.MALE)
    address = models.CharField(max_length=400, null=True, blank=True)
    send_news = models.BooleanField(default=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        db_table = 'user_custom'


class Organization(models.Model):
    class OrganizationTypeChoices(models.TextChoices):
        SCHOOL = 'school', 'Школа'
        KINDERGARTEN = 'kindergarten', 'Детский сад'
        OTHER = 'other', 'Другое'

    organization_type = models.CharField(max_length=15, choices=OrganizationTypeChoices.choices)
    name = models.CharField(max_length=100)


class ParticipantModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=participant_directory_path, null=True, blank=True)
    organization_type = models.CharField(max_length=15, choices=Organization.OrganizationTypeChoices.choices,
                                         default=Organization.OrganizationTypeChoices.SCHOOL)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='participants', null=True,
                                     blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        db_table = 'user_participants'


class JudgeModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=judge_directory_path, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Judge'
        verbose_name_plural = 'Judges'
        db_table = 'user_judges'
