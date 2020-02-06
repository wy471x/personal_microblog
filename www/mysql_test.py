#!/usr/bin/env python
# coding=utf-8

__author__ = 'Dunk Wan'

import orm
import asyncio, random, string
from models import User, Blog, Comment, next_id

#email attribute for Users
def random_email():
    email = random.randint(100000000, 999999999)
    return str(email) +'@example.com'

def random_name():
    return ''.join(random.sample(string.ascii_letters + string.digits, 5))

#content attribute for Blogs
def random_content():
    return ''.join(random.sample(string.ascii_letters + string.digits, 50))

async def test(loop):
    await orm.create_pool(loop=loop, user='www_data', password='www_data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    b = Blog(user_name='Dunk', name='Test', user_image='about:blank', summary='Kobe Bryant is great basketball player!')
    c = Comment(user_name='Dunk', user_image='about:blank')
    #insert test
    #Users
    #for x in range(100):
    #    u['id'] = next_id()
    #    u['email'] = random_email()
    #    u['name'] = random_name()
    #    await u.save()
    #for item in u:
    #    print(item)
    #Blogs
    #for x in range(100):
    #    b['id'] = next_id()
    #    b['user_id'] = next_id()
    #    b['name'] = random_name()
    #    b['content'] = random_content()
    #    await b.save()
    #for item in b:
    #    print(item)
    #Comments
    #for x in range(100):
    #    c['id'] = next_id()
    #    c['blog_id'] = next_id()
    #    c['user_id'] = next_id()
    #    c['content'] = random_content()
    #    await c.save()
    #for item in c:
    #    print(item)

    #select test
    #Users
    #u = await User.findAll(where='name like ?', args=['%a%'], orderBy='name asc', limit=(0, 10))
    #for item in u:
    #    print(item)
    #u = await User.findAll()
    #for item in u:
    #    print(item)
    #Blogs
    #b = await Blog.findAll(where='name like ?', args=['%a%'], orderBy='name asc', limit=(0,10))
    #for item in b:
    #    print(item)
    #Comments
    #c = await Comment.findAll(where='blog_id like ?', args=['%1%'], orderBy='blog_id asc', limit=(0,10))
    #for item in c:
    #    print(item)

    #update test
    #Users
    #u = await User.find('001580317138898fc8e74cbd70a454d950551283a5cb886000')
    #u['passwd'] = '123'
    #await u.update()
    #print(u)
    #Blogs
    #b = await Blog.find('00158035349548360e96cece8784a3ba6dafecdfd23de16000')
    #print('before:')
    #print(b)
    #b['content'] = random_content()
    #await b.update()
    #print('after:')
    #print(b)
    #Comments
    #c = await Comment.find('0015803546742359f39f154c9c447d9ab756439838c1965000')
    #print('before:')
    #print(c)
    #c['content'] = random_content()
    #await c.update()
    #print('after:')
    #print(c)

    #delete test
    #Users
    #u = await User.find('00158031713939062b19b696dcb44328825cc2c8a4f487a000')
    #await u.remove()
    #print(u)
    #Blogs
    #b = await Blog.find('00158035349608091490fd48eb84a0db7281f805a4a309c000')
    #print('before:')
    #print(b)
    #await b.remove()
    #b = await Blog.find('00158035349608091490fd48eb84a0db7281f805a4a309c000')
    #print('after:')
    #print(b)
    #Comments
    #c = await Comment.find('001580354674679049d1738e5134c27bf2836d51a99d99b000')
    #print('before:')
    #print(c)
    #await c.remove()
    #c = await Comment.find('001580354674679049d1738e5134c27bf2836d51a99d99b000')
    #print('after:')
    #print(c)

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()

for x in test(loop):
    pass
