from django.db import models


class ActiveData(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # reminder : json format reminder  times based on Crontab
    reminder = models.CharField(max_length=200)
    # action : json {"function:{"name":"",kargs:{}}}
    action = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ":" + self.description

class DataTemplate(models.Model):
    subject = models.CharField(max_length=50)
    sub_subject = models.CharField(max_length=50)
    template = models.CharField(max_length=500)


    def __str__(self):
        return self.subject + ":" + self.sub_subject+ ":" + self.template

class Data(models.Model):
    subject = models.CharField(max_length=50)
    sub_subject = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=500)


    def __str__(self):
        return self.subject + ":" + self.sub_subject+ ":" + self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sub_Subject(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

