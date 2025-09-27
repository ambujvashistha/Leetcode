# Write your MySQL query statement below

select pt.project_id, round(avg(et.experience_years),2) as average_years
from project pt
inner join employee et
on pt.employee_id=et.employee_id
group by pt.project_id;