#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Models for user, blog, comment.
"""

__author__ = 'duke.wu'

import time
import uuid
from orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)', default='')
    admin = BooleanField(default=0)
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)', default='')
    created_at = FloatField(default=time.time)
    site = StringField(ddl='varchar(500)', default='')
    private = BooleanField(default=1)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    label = StringField(ddl='varchar(50)')
    read_total =  IntegerField(default=0)
    limit = BooleanField()
    created_at = FloatField(default=time.time)
    latestupdated_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    parent_id = StringField(ddl='varchar(50)')
    at_who = StringField(ddl='varchar(50)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Label(Model):
    __table__ = 'labels'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(8)')
    label = StringField(ddl='varchar(50)')
    explain = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


'''
class Permission(object):
    LOGIN = 0x01
    EDITOR = 0x02
    OPERATOR = 0x04
    ADMINISTER = 0xff
    PERMISSION_MAP = {
        LOGIN:('login','Login user'),
        EDITOR:('editor','Editor'),
        OPERATOR:('op','Operator'),
        ADMINISTER:('admin','Super administrator')
    }

class Role(Model):
    __table__ = 'role'

    id = IntegerField(primary_key=True )
    name = StringField(ddl='varchar(50)')
    permissions = IntegerField(primary_key=True, default=Permission.LOGIN )
    description = StringField(ddl='varchar(100)')
'''
