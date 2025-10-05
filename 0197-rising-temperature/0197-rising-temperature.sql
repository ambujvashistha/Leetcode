# Write your MySQL query statement below

select w1.id 
from (select * from weather order by recordDate) w1
inner join weather w2
on DATE_SUB(w1.recordDate, INTERVAL 1 DAY)=w2.recordDate and w1.temperature>w2.temperature;
