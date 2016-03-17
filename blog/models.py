#coding:utf-8
from django.db import models
from django import forms
# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()

    def save(self,*args,**kwargs):
        if self.name == "admin":
            return
        else:
            super(Blog,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog=models.ForeignKey(Blog)
    headline=models.CharField(max_length=255)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    authors=models.ManyToManyField(Author)
    n_comments=models.IntegerField()
    n_pingbacks=models.IntegerField()
    rating=models.IntegerField()

    def __str__(self):
        return self.headline
    def __unicode__(self):
        return self.headline

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()
    def __str__(self):
        return self.first_name+'\t'+self.birth_date
    def __unicode__(self):
        return self.first_name+'\t'+self.birth_date
    def baby_boomer_status(self):
        import datetime
        if self.birth_date<datetime.datetime(1945,8,1):
            return "Pre"
        elif self.birth_date<datetime.date(1965,1,1):
            return "Baby"
        else:
            return "Post"

    def _get_full_name(self):
        return '%s %s' % (self.first_name,self.last_name)
    full_name=property(_get_full_name)


class OrderedPerson(Person):
    class Meta:
        proxy=True
        ordering=["last_name"]

class Ox(models.Model):
    horn_length=models.IntegerField()
    class Meta:
        ordering=["horn_length"]
        verbose_name_plural="oxen"

class Maner(models.Model):
    name=models.CharField(max_length=32)
    brithday=models.DateField()
    class Meta:
        verbose_name_plural="男人们"
        verbose_name="男人"
        db_table="t_man"

class CommonInfo(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    class Meta:
        abstract=True
        ordering=['name']

#子类的meta会继承父类的meta的属性
class Student(CommonInfo):
    home_group=models.CharField(max_length=5)
    class Meta(CommonInfo.Meta):
        db_table='student_info'

class OtherModel(models.Model):
    soso=models.CharField(max_length=10)

#基础类中含有manytomany的字段 子类会继承  但是子类的字段名称应该动态改变
class Base(models.Model):
    m2m=models.ManyToManyField(OtherModel,related_name="%(app_label)s_%(class)s_related")
    class Meta:
        abstract=True

class ChildA(Base):
    otherCol=models.CharField(max_length=32)

class ChildB(Base):
    otherCol=models.CharField(max_length=32)

#多表继承
class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class UploadFileForm(forms.Form):
    title=forms.CharField(max_length=50)
    file=forms.FileField()