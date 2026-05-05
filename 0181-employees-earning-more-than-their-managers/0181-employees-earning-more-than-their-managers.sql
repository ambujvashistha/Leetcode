# Write your MySQL query statement below

select et.name as Employee
from Employee as et
inner join Employee as ot
on et.managerId=ot.id and et.salary>ot.salary;