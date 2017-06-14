from django.db import models


class Schedule(models.Model):
    hour = models.IntegerField(default=12)
    minute = models.IntegerField(default=59)

    def __str__(self):
        return "%i:%i" % (self.hour, self.minute)


class Line(models.Model):
    letter = models.CharField(max_length=2)
    directionA = models.CharField(max_length=255)
    directionB = models.CharField(max_length=255)

    def __str__(self):
        return self.letter


class Driver(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Train(models.Model):
    name = models.CharField(max_length=255)
    line = models.ForeignKey(Line, on_delete=models.CASCADE, blank=True, null=True)
    schedules = models.ManyToManyField(Schedule, blank=True, null=True)
    driver = models.OneToOneField(Driver, blank=True, null=True)

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=255)
    lines = models.ManyToManyField(Line, blank=True, null=True)

    def __str__(self):
        return self.name
