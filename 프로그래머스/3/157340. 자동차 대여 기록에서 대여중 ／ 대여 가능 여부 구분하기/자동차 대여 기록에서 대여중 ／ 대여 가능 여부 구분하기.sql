-- 코드를 입력하세요
SELECT CAR_ID, 
IF(car_id in 
   (select car_id 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY  
    WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE ), '대여중', '대여 가능') as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc