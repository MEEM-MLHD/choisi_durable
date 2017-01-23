# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='images')
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = u"Image"

    def __unicode__(self):
        return self.title


class ActorKeyword(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Mot-clef acteur"

    def __unicode__(self):
        return self.label


class ExperienceKeyword(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Mot-clef expérience"

    def __unicode__(self):
        return self.label


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Contact"

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Actor(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="actors/logo")
    address = models.TextField()
    geo = models.PointField()
    website = models.URLField()
    description = models.TextField()
    contacts = models.ManyToManyField(Contact)
    images = models.ManyToManyField(Image)
    keywords = models.ManyToManyField(ActorKeyword)
    convention = models.BooleanField()

    class Meta:
        verbose_name = u"Acteur"

    def __unicode__(self):
        return self.name


class Participant(models.Model):
    logo = models.ImageField(upload_to="participants/logo")
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Participant"

    def __unicode__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255, blank=True)
    featured_image = models.ImageField(upload_to="experiences/feature-image")
    zip_code = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    fulfilled = models.BooleanField()
    contacts = models.ManyToManyField(Contact)
    keywords = models.ManyToManyField(ExperienceKeyword)
    participants = models.ManyToManyField(Participant)

    featured = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Expérience"

    def __unicode__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to="events/feature-image")
    description = models.TextField()
    publication_date = models.DateField()
    deadline_date = models.DateField()

    featured = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Evénement"

    def __unicode__(self):
        return self.title

