-- 코드를 입력하세요 
SELECT PRODUCT_CODE, sum(PRICE * SALES_AMOUNT) as SALES
from PRODUCT inner join OFFLINE_SALE using (PRODUCT_ID)
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE asc
