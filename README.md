# News Report

This is a log report project using _python_ and _PostgreSQL_.

Created 2 views for my querys.

`create view error_count as select TO_CHAR(time::DATE, 'dd/mm/yy') as day, count(TO_CHAR(time::DATE, 'dd/mm/yy')) as cnt from log group by day, status having status != '200 OK'`

`create view success_count as select TO_CHAR(time::DATE, 'dd/mm/yy') as day, count(TO_CHAR(time::DATE, 'dd/mm/yy')) as cnt from log group by day, status having status = '200 OK'`
