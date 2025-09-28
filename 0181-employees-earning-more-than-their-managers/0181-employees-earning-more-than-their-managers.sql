# Write your MySQL query statement below

select et1.name as Employee
from Employee et1
inner join Employee et2
on et1.managerId=et2.id
where et1.salary>et2.salary;