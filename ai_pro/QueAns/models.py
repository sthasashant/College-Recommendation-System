from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    college = models.ForeignKey(College, related_name='review', on_delete="cascade")
    pass_result = models.IntegerField()
    extra_curriculum = models.IntegerField()
    expensive = models.IntegerField()
    dress = models.IntegerField()
    strict = models.IntegerField()
    science = models.IntegerField()
    management = models.IntegerField()

    variable = models.FloatField(default=0.0)


    def __str__(self):
        return self.college.name


class Cos_Sim(models.Model):
    college = models.ForeignKey(College, on_delete="cascade")
    similarity = models.IntegerField(default=0)

    def __str__(self):
        return self.college.name
