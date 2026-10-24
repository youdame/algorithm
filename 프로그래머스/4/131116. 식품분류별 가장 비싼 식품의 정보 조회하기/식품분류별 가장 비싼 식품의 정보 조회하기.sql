with max_table as (
SELECT CATEGORY, max(price) as MAX_PRICE
from FOOD_PRODUCT
where CATEGORY in ('과자', '국', '김치', '식용유')
group by category
)

select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (category, price) in (select category, MAX_PRICE from max_table) 
ORDER BY MAX_PRICE DESC;