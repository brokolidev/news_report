#!/usr/bin/env python3
#
# A buggy web service in need of a database.
import datetime
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

sql = """ select a.title, count(l.path) as cnt from log as l
        join articles as a
        on l.path=CONCAT('/article/',a.slug)
        group by l.path, a.title order by count(l.path) desc limit 3 """
c.execute(sql)
rows = c.fetchall()
print("")
print("The Most 3 Popular Articles")
for row in rows:
    print("Title : {} | View : {}".format(row[0], row[1]))

sql = """ select au.name, count(l.path) from log as l
        join articles as a on l.path=CONCAT('/article/',a.slug)
        join authors as au on au.id=a.author
        group by au.name, l.path order by count(l.path) desc limit 3 """
c.execute(sql)
rows = c.fetchall()
print("")
print("The Most 3 Popular Authors")
for row in rows:
    print("Author : {} | View : {}".format(row[0], row[1]))

# Created 2 views
sql = """ select sc.day, round((100.0 * (ec.cnt::numeric/sc.cnt::numeric)), 1)
        as err_rate from success_count as sc
        join error_count as ec on ec.day=sc.day
        where round((100.0 * (ec.cnt::numeric/sc.cnt::numeric)), 1) > 1 """
c.execute(sql)
logs = c.fetchall()
print("")
print("More than 1% of errors on")
for log in logs:
    print("Date : {} | Error Rate : {}%".format(log[0], log[1]))
print("")

db.close()
