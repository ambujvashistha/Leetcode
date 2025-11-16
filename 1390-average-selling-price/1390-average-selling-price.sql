# Write your MySQL query statement below
select pt.product_id,ifnull(round((sum(pt.price * ut.units)/sum(ut.units)),2),0) as average_price
from prices pt
left join unitssold ut
on pt.product_id=ut.product_id and (ut.purchase_date>= pt.start_date and ut.purchase_date <= pt.end_date)
group by pt.product_id
order by pt.product_id;