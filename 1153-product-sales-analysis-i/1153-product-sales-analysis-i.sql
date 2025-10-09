# Write your MySQL query statement below
select pt.product_name, st.year, st.price
from product pt
inner join sales st
on st.product_id=pt.product_id;