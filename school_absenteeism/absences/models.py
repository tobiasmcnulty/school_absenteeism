from django.db import models
from localflavor.us.models import PhoneNumberField


class School(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name


class HomeRoom(models.Model):
    GRADE_CHOICES = (
        (0, 'K'),
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        (5, '5th'),
        (6, '6th'),
        (7, '7th'),
        (8, '8th'),
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th'),
    )
    school = models.ForeignKey(School)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    grade = models.IntegerField(max_length=20, choices=GRADE_CHOICES)

    def __unicode__(self):
        return u'{0}, {1} ({2})'.format(self.last_name, self.first_name, self.school)


class Parent(models.Model):
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField()

    def __unicode__(self):
        return u', '.join([self.last_name, self.first_name])


class Student(models.Model):
    parent = models.ForeignKey(Parent)
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=255)

    def __unicode__(self):
        return u', '.join([self.last_name, self.first_name])


class AbsenceReason(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.label


class Absence(models.Model):
    student = models.ForeignKey(Student)
    home_room = models.ForeignKey(HomeRoom)
    date = models.DateField()
    reason = models.ForeignKey(AbsenceReason)

    def __unicode__(self):
        return u'{0} absent from {1} on {2}'.format(self.student, self.home_room, self.date)
