# News Report

News Report is a simple script for reporting some factors from the data provided by Udacity. This script can answer those 3 questions. Also this project was created by using _python_ and _PostgreSQL_.
Q1. What are the most popular three articles of all time?
Q2. Who are the most popular article authors of all time?
Q3. On which days did more than 1% of requests lead to errors?

## The database

The database has 3 tables.
- articles
- authors
- log
The log table has a database row for each time a reader access a web page.

## Installation & Usage

Clone the GitHub repository
```
$ git clone https://https://github.com/brokolidev/news_report.git
$ cd news_report
```

Download database from [HERE](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and import them to your database.
You will need to unzip this file after downloading it. The file inside is called newsdata.sql
```
psql -d news -f newsdata.sql
```

Create 2 views for some calcuation.
```
psql -d news -f create_views.sql
```
OR you can just copy and paste this SQL query.
```
create view error_count as select TO_CHAR(time::DATE, 'dd/mm/yy') as day, count(TO_CHAR(time::DATE, 'dd/mm/yy')) as cnt from log group by day, status having status != '200 OK';
create view success_count as select TO_CHAR(time::DATE, 'dd/mm/yy') as day, count(TO_CHAR(time::DATE, 'dd/mm/yy')) as cnt from log group by day, status having status = '200 OK';
```

Run the script.
```
$ python reporter.py
```
