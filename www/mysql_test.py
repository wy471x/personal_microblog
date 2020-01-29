#!/usr/bin/env python
# coding=utf-8

__author__ = 'Dunk Wan'

import orm
import asyncio, random, string
from models import User, Blog, Comment, next_id

def random_email():
    email = random.randint(100000000, 999999999)
    return str(email) +'@example.com'

def random_name():
    return ''.join(random.sample(string.ascii_letters + string.digits, 5))

async def test(loop):
    await orm.create_pool(loop=loop, user='www_data', password='www_data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    #insert test
    #for x in range(100):
    #    u['id'] = next_id()
    #    u['email'] = random_email()
    #    u['name'] = random_name()
    #    await u.save()
    #for item in u:
    #    print(item)

    #select test
    #u = await User.findAll(where='name like ?', args=['%a%'], orderBy='name asc', limit=(0, 10))
    #for item in u:
    #    print(item)

    #update test
    #u = await User.find('001580317138898fc8e74cbd70a454d950551283a5cb886000')
    #u['passwd'] = '123'
    #await u.update()
    #print(u)

    #delete test
    #u = await User.find('00158031713939062b19b696dcb44328825cc2c8a4f487a000')
    #await u.remove()
    #print(u)
    

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()

for x in test(loop):
    pass
