# Write your MySQL query statement below
with newTable as (
    select email,count(email) 
    from person 
    group by email 
    having count(email) >= 2
    )
select email 
from  newtable;