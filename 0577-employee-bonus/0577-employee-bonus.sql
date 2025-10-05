# Write your MySQL query statement below

select et.name,bt.bonus
from employee et
left join bonus bt
on et.empid=bt.empid
where bt.bonus<1000 or bt.bonus is null;