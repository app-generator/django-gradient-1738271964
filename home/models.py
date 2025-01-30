# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Club(models.Model):

    #__Club_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    #__Club_FIELDS__END

    class Meta:
        verbose_name        = _("Club")
        verbose_name_plural = _("Club")


class Player(models.Model):

    #__Player_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    preferred_foot = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    current_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    previous_club = models.ForeignKey(Club, on_delete=models.CASCADE)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")


class Match(models.Model):

    #__Match_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    home_team = models.ForeignKey(Club, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, on_delete=models.CASCADE)

    #__Match_FIELDS__END

    class Meta:
        verbose_name        = _("Match")
        verbose_name_plural = _("Match")


class Performance(models.Model):

    #__Performance_FIELDS__
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    non_penalty_goals = models.IntegerField(null=True, blank=True)
    shots_total = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    pass_completion = models.IntegerField(null=True, blank=True)
    progressive_passes = models.IntegerField(null=True, blank=True)
    progressive_carries = models.IntegerField(null=True, blank=True)
    successful_take_ons = models.IntegerField(null=True, blank=True)
    touches = models.IntegerField(null=True, blank=True)
    tackles = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    clearances = models.IntegerField(null=True, blank=True)
    aerials_won = models.IntegerField(null=True, blank=True)
    technical_skills = models.IntegerField(null=True, blank=True)
    game_sense = models.IntegerField(null=True, blank=True)
    ball_control = models.IntegerField(null=True, blank=True)
    sprinting_speed = models.IntegerField(null=True, blank=True)
    handling_speed = models.IntegerField(null=True, blank=True)
    winning_mindset = models.IntegerField(null=True, blank=True)
    intrinsic_motivation = models.IntegerField(null=True, blank=True)

    #__Performance_FIELDS__END

    class Meta:
        verbose_name        = _("Performance")
        verbose_name_plural = _("Performance")


class Scouts(models.Model):

    #__Scouts_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    clubs = models.ForeignKey(Club, on_delete=models.CASCADE)

    #__Scouts_FIELDS__END

    class Meta:
        verbose_name        = _("Scouts")
        verbose_name_plural = _("Scouts")



#__MODELS__END
