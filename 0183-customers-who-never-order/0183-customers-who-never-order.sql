# Write your MySQL query statement below
select name as Customers
from customers 
where id not in (
    select ct.id 
    from customers ct
    inner join orders ot
    on ct.id=ot.customerID
);