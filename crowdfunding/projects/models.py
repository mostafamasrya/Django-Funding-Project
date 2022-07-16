from django.core.validators import RegexValidator
from django.db import models

class Usercrowd(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField( max_length=11, blank=True)
    profile_img = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=False)
    expire_date = models.DateTimeField()
    birthdate = models.DateField(null=True)
    country = models.CharField(null=True,max_length=50)
    facebooklink = models.URLField(null=True)
    is_admin = models.BooleanField(default=False)



class Projects(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    total_target = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)



class ProjectsImages(models.Model):
    images = models.ImageField(upload_to='images/')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

class ProjectsTages(models.Model):
    tags = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=100)
    image_cat = models.ImageField(upload_to='images/')
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)


class Donation(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)
    donation_value = models.IntegerField()


class Rate(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)
    rate = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment = models.TextField(default='')


class CommentReports(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)



class ProjectReports(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    user = models.ForeignKey(Usercrowd, on_delete=models.CASCADE)