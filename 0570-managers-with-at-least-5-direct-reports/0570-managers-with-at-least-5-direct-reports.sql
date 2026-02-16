# Write your MySQL query statement below
with ok as (select managerId, count(id) as final
from Employee
group by managerId)
select et.name
from Employee et
inner join ok 
on et.id = ok.managerId and ok.final>=5;