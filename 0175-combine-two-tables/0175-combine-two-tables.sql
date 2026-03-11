select pt.firstName, pt.lastName, ad.city, ad.state
from person pt
left join address ad
on pt.personid=ad.personid;