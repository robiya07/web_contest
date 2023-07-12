from django.db import models
from django.utils.text import slugify
from datetime import datetime


def contest_directory_path(instance, filename):
    today = datetime.now()
    path = f"contest/contest_images/{today.year}/{today.month}/{today.day}/{filename}"
    return path


def prize_directory_path(instance, filename):
    today = datetime.now()
    return f"contest/prize_images/{today.year}/{today.month}/{today.day}/{filename}"


# Create your models here.
class ContestModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=contest_directory_path)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            while ContestModel.objects.filter(slug=self.slug).exists():
                slug = ContestModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contest'
        verbose_name_plural = 'Contests'
        db_table = 'cont_contests'


class RuleModel(models.Model):
    contest = models.ForeignKey(to=ContestModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.contest.name

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'
        db_table = 'cont_rules'


class PrizeModel(models.Model):
    contest = models.ForeignKey(to=ContestModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=prize_directory_path)
    place = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Prize'
        verbose_name_plural = 'Prizes'
        db_table = 'cont_prizes'
