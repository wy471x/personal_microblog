#!/usr/bin/env python
# coding=utf-8

__author__ = 'Dunk Wan'

'''
 URL  handlers
'''

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    #for item in users:
    #    print(item)
    return {
        '__template__': 'test.html',
        'users': users
    }
