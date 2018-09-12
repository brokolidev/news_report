#!/usr/bin/env python3
#
# A buggy web service in need of a database.
import datetime
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

sql = "select substring(path from 10) as slug, count(path) as views \
    from log group by path \
    having path not in ('/', '/spam-spam-spam-humbug', '&20%20%20') \
    order by views desc limit 3"
c.execute(sql)
logs = c.fetchall()
print("")
print("The Most 3 Popular Articles")
for log in logs:
    slug = log[0]
    sql = "select title from articles where slug=%s"
    c.execute(sql, [slug])
    articles = c.fetchall()
    title = articles[0][0]
    print("Title : {} | view : {}".format(title, log[1]))

print("")
print("The Most 3 Popular Authors")
for log in logs:
    slug = log[0]
    sql = "select author from articles where slug=%s"
    c.execute(sql, [slug])
    article = c.fetchall()
    author_id = article[0][0]
    sql = "select name from authors where id=%s"
    c.execute(sql, [author_id])
    author = c.fetchall()
    author_name = author[0][0]
    print("Author : {} | view : {}".format(author_name, log[1]))

# Created 2 views
sql = "select sc.day, round((100.0 * (ec.cnt::numeric/sc.cnt::numeric)), 1) \
        as err_rate from success_count as sc \
        join error_count as ec on ec.day=sc.day \
        where round((100.0 * (ec.cnt::numeric/sc.cnt::numeric)), 1) > 1"
c.execute(sql)
logs = c.fetchall()
print("")
print("More than 1% of errors on")
for log in logs:
    print("Date : {} | Error Rate : {}%".format(log[0], log[1]))

print("")

db.close()
