# Write your MySQL query statement below
select ok.customer_number
from (
    select customer_number,count(customer_number)
    from orders
    group by customer_number
    order by count(customer_number) desc
    limit 1
) as ok;