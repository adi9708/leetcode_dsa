# Write your MySQL query statement below
Select 
case 
when id = (Select max(id) from seat) and id % 2 = 1 then id
when id % 2 = 1 then id + 1 else id - 1 END as id, 
student
from Seat
order by id
