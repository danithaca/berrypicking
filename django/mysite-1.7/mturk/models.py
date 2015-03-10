from django.db import models


class Survey(models.Model):
    """ Imported from controlTower_CSATsurvey; the interface between mturk and the other part of the system """

    # this should be a foreign key to controlTower_CSATsurvey.question_session_id
    # since that table is not a django model, we'll just use IntegerField instead.
    ref = models.IntegerField(primary_key=True)
    # this is the survey feedback on "dissatisfied other". the text to be categorized.
    feedback = models.TextField()

    # language code: en, pt, es, etc. blank means it's not processed through google translate yet.
    language_code = models.CharField(max_length=2, blank=True)
    # google translation
    gtrans = models.TextField(blank=True)
    # translation from turker1
    turk1 = models.TextField(blank=True)
    # translation from turker2
    turk2 = models.TextField(blank=True)

    # concat results from mturk.
    categorization_result = models.CharField(max_length=100)
    # final results from mturk (processed if we got multiple results from mturk).
    category = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)


# below is mturk-realted stuff


class HIT(models.Model):
    """ data model for Mturk HIT """
    hit_id = models.CharField(max_length=30, primary_key=True)
    hit_type_id = models.CharField(max_length=30)
    # timestamp of when the db record is created, not when the hit was created on mturk.
    created = models.DateTimeField(auto_now_add=True)


class Assignment(models.Model):
    """ data model for Mturk Assignment, ie, workers submission """
    assignment_id = models.CharField(max_length=30, primary_key=True)
    hit = models.ForeignKey(HIT, db_column='hit_id')
    worker_id = models.CharField(max_length=14)
    # timestamp of when the db record is created, not when the assignment was accepted/submitted.
    created = models.DateTimeField(auto_now_add=True)


class HITSurvey(models.Model):
    """ hit for the survey categorization task"""
    hit = models.OneToOneField(HIT, db_column='hit_id', primary_key=True)
    # use foreign key here because we might have multiple HITs for one survey
    survey = models.ForeignKey(Survey)


class AssignmentSurvey(models.Model):
    """ assignment for the survey categorization task"""
    assignment = models.OneToOneField(Assignment, db_column='assignment_id', primary_key=True)
    # this saves mturk categorization results to the hit->ref survey.
    category = models.CharField(max_length=50)


class HITTranslation(models.Model):
    """ hit for the translation task"""
    hit = models.OneToOneField(HIT, db_column='hit_id', primary_key=True)
    # use foreign key here because we might have multiple HITs for one survey
    survey = models.ForeignKey(Survey)


class AssignmentTranslation(models.Model):
    """ assignment for the translation task"""
    assignment = models.OneToOneField(Assignment, db_column='assignment_id', primary_key=True)
    translated = models.TextField()
