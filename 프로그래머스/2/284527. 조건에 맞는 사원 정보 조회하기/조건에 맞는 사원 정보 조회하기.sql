with sum_score as (
select EMP_NO, sum(score) as score
from hr_grade
where year = 2022
group by emp_no)



select score,	e.EMP_NO,	EMP_NAME,	POSITION,	EMAIL
from hr_employees e
join sum_score s
on e.emp_no = s.emp_no
order by score desc
limit 1
