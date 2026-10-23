
with recursive time_table as (
    select 0 as hour
    
    union all
    
    select hour + 1
    from time_table
    where hour < 23
)

select T.hour , IFNULL(A.count, 0) as count
from time_table T
left join 
(select HOUR(DATETIME) as hour, count(*) as count
from ANIMAL_OUTS
group by hour) as A
ON T.hour = A.hour