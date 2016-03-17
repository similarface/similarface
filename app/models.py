#coding:utf-8
from django.db import models

# Create your models here.


class Person(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Group(models.Model):
    name=models.CharField(max_length=128)
    members=models.ManyToManyField(Person,through='Membership')
    def __str__(self):
        return self.name

class Membership(models.Model):
    person=models.ForeignKey(Person)
    group=models.ForeignKey(Group)
    date_joined=models.DateField()
    invite_reason=models.CharField(max_length=64)

class Musician(models.Model):
    SEX_CHOICES=(
        ('1','男'),
        ('0','女'),
        ('2','未知'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex=models.CharField(max_length=1,choices=SEX_CHOICES,default='2')
    instrument=models.CharField(max_length=100)



class Album(models.Model):
    #音乐作者
    artist=models.ForeignKey(Musician)
    #专辑名
    name=models.CharField(max_length=100,null=False)
    #发行日期
    release_date=models.DateField(blank=True,null=True)
    #热度
    num_starts=models.IntegerField(blank=False,null=True)

class Fruit(models.Model):
    name=models.CharField(max_length=100,primary_key=True)


class Manufacturer(models.Model):
    factoryName=models.CharField(max_length=100)

class Car(models.Model):
    carid=models.CharField(max_length=68)
    manufacturer=models.ForeignKey(Manufacturer)

class Topping(models.Model):
    name=models.CharField(max_length=30)

class Pizza(models.Model):
    pname=models.CharField(max_length=10)
    toppings=models.ManyToManyField(Topping)



#地址
class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Restaurant(models.Model):
    place=models.OneToOneField(Place,primary_key=True)
    servers_hot_dogs=models.BooleanField(default=False)
    servers_pizza=models.BooleanField(default=False)
    servers_kfc=models.BooleanField(default=False)
    def __str__(self):
        return self.place.name
    def __unicode__(self):
        return self.place.name

#服务员
class Waiter(models.Model):
    restaurant=models.ForeignKey(Restaurant)
    name=models.CharField(max_length=50)
    def __str__(self):
        return "%s服务于%s" % (self.name, self.restaurant)

    def __unicode__(self):
        return "%s服务于%s" % (self.name, self.restaurant)