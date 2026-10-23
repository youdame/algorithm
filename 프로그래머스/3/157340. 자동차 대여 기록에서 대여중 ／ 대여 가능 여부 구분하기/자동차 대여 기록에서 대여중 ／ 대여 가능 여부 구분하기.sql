-- 코드를 입력하세요
SELECT CAR_ID, 
MAX(CASE 
    WHEN '2022-10-16' between START_DATE and END_DATE THEN '대여중'
    ELSE '대여 가능'


END) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc