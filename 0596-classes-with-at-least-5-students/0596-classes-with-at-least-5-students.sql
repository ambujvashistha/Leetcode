# Write your MySQL query statement below
with ok as (select class, count(student)
from Courses
group by class
having count(student)>=5)
select class from ok;