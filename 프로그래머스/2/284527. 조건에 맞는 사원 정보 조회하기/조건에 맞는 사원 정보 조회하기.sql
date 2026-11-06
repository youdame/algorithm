with sum_score as (
select EMP_NO, sum(score) as score
from hr_grade
where year = 2022
group by emp_no)



select s.score, e.EMP_NO,	EMP_NAME,	POSITION,	EMAIL
from hr_employees e
join sum_score s
on e.emp_no = s.emp_no
where score = (select max(score) from sum_score)
