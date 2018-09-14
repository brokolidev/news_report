create view error_count as select TO_CHAR(time::DATE, 'dd/mm/yy') as day, count(TO_CHAR(time::DATE, 'dd/mm/yy')) as cnt from log group by day, status having status != '200 OK';
create view success_count as select TO_CHAR(time::DATE, 'dd/mm/yy') as day, count(TO_CHAR(time::DATE, 'dd/mm/yy')) as cnt from log group by day, status having status = '200 OK';
