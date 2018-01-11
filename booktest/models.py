# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Goods(models.Model):
    name = models.CharField(max_length=150)
    cate_id = models.IntegerField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    is_show = models.TextField()  # This field type is a guess.
    is_saleoff = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsBrands(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'goods_brands'


class GoodsCates(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'goods_cates'


class TestIndex(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_index'
