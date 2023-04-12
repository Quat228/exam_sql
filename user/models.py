from django.db import models
from datetime import date, timedelta


class Language(models.Model):
    name = models.CharField(max_length=30)
    month = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if self.phone_number[0:4] != '+996':
            if self.phone_number[0] == '0':
                self.phone_number = list(self.phone_number)
                self.phone_number.pop(0)
                self.phone_number = ''.join(self.phone_number)
            self.phone_number = '+996' + self.phone_number
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=40, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=30, choices=(
        ('windows', 'Windows'),
        ('macos', 'MacOS'),
        ('linux', 'Linux')
    ))

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=30, null=True, blank=True)
    experience = models.DateField()
    students = models.ManyToManyField(Student, related_name='mentors', through='Course')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, models.CASCADE, related_name='courses')
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='courses')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses')

    def get_end_date(self):
        return self.date_started + timedelta(days=self.language.month * 30)

    def __str__(self):
        return self.name



