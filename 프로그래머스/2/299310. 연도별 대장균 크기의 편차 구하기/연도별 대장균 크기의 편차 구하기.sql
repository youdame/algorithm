with max_colony_table as (select YEAR(DIFFERENTIATION_DATE) as year, max(size_of_colony) as max_colony
from ecoli_data
group by YEAR(DIFFERENTIATION_DATE))


select m.year, max_colony - SIZE_OF_COLONY as YEAR_DEV, id
from ecoli_data 
join max_colony_table m 
on m.year = YEAR(DIFFERENTIATION_DATE)
order by m.year, YEAR_DEV