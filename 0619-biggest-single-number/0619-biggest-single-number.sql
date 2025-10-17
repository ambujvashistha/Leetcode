# Write your MySQL query statement below
select ifnull(sub.num,max(num)) as num
from(select num,count(num) 
from MyNumbers
group by num
having count(num)=1
order by num desc) as sub
limit 1;