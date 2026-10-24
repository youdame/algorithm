-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) as YEAR, month(SALES_DATE) as month, GENDER, count( DISTINCT S.USER_ID) as users
FROM ONLINE_SALE S
JOIN USER_INFO I
ON  S.USER_ID = I.USER_ID
group by year, month, gender
having gender is not null
order by year, month, gender