# Write your MySQL query statement below
SELECT distinct a.num as ConsecutiveNums from Logs a 
join Logs b on a.id=b.id+1 and a.num=b.num
join logs c on a.id=c.id+2 and a.num=c.num;