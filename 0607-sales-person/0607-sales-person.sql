# Write your MySQL query statement below

-- select sp.sales_id,sp.name,sp.salary,sp.commission_rate,sp.hire_date
-- from SalesPerson as sp
-- left join orders ot
-- on sp.sales_id=ot.sales_id
-- left join Company as ct
-- on ot.com_id=ct.com_id and ct.name!="RED";

-- with ok as (
--     select ot.sales_id
--     from orders ot
--     inner join Company as ct
--     on ot.com_id=ct.com_id and ct.name="RED"
-- )
select name
from SalesPerson 
where sales_id not in (
    select ot.sales_id
    from orders ot
    inner join Company as ct
    on ot.com_id=ct.com_id and ct.name="RED"
) ;