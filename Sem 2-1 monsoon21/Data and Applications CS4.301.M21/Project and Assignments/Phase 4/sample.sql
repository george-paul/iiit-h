-- one

select CustNumber
from Customer 
where Arrived = 0 and ResPhone = '2718283141'
order by CustNumber;

update Customer set Arrived = true 
where CustNumber = 10;


-- two

select sum(m.ItemPrice) 
from Dish as d, Menu_Item as m, Ordered as o 
where d.ItemName = m.ItemName and d.DishNo = o.DishNo and o.OrderNo = 1;

-- three

select Ord.OrderNo, Dish.DishNo 
from Ord join Taken_ETA on Ord.TakenTime = Taken_ETA.TakenTime 
join Ordered on Ordered.OrderNo = Ord.OrderNo 
join Dish on Dish.DishNo = Ordered.DishNo 
where ETA < NOW() and Dish.Status != 'Delivered';



select * 
from Dish as d, Menu_Item as m, Ordered as o 
where d.ItemName = m.ItemName and d.DishNo = o.DishNo and o.OrderNo = 1;