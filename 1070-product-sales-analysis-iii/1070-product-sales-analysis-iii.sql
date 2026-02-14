# Write your MySQL query statement below
with OK as (select product_id, min(year) as first_year, quantity, price
from Sales 
group by product_id)
select st.product_id, st.year as first_year, st.quantity, st.price
from sales as st
inner join ok 
on st.product_id = ok.product_id and st.year=ok.first_year;