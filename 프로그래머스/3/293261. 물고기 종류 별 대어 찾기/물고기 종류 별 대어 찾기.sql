-- 코드를 작성해주세요
with max_table as (select fish_type, max(length) as length
from fish_info f
group by f.fish_type)



select ID,	FISH_NAME,	LENGTH
from fish_info f
join fish_name_info n
on f.fish_type = n.fish_type
where (f.fish_type, length) in (select * from max_table)