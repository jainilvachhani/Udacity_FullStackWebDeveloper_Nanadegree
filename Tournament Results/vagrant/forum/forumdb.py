#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Get posts from database.
def GetAllPosts():
    DB = psycopg2.connect("dbname = forum")
    c = DB.cursor()
    c.execute("SELECT time,content FROM posts ORDER BY time DESC")
    posts = ({'content' : str(row[1]), 'time' : str(row[0]) } for row in c.fetchall())
    DB.close()
    return posts	

## Add a post to the database.
def AddPost(content):
    DB = psycopg2.connect("dbname = forum")
    c = DB.cursor()
    bleached_name = bleach.clean(content)
    c.execute("INSERT INTO posts (content) VALUES (%s)", (bleached_name,))
    c.execute("DELETE from posts where content = 'cheese'")
    DB.commit()
    DB.close()
