from django.db.models import Model, \
    CharField, PositiveIntegerField, BooleanField


class Advertisement(Model):
    name = CharField(max_length=200)
    author = CharField(max_length=100)
    price = PositiveIntegerField()
    description = CharField(max_length=2000)
    address = CharField(max_length=200)
    is_published = BooleanField()


class Category(Model):
    name = CharField(max_length=200)
