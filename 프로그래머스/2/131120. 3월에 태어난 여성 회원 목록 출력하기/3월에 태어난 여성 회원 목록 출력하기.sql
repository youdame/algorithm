-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, to_char(DATE_OF_BIRTH, 'yyyy-mm-dd') as DATE_OF_BIRTH
from MEMBER_PROFILE
where  TLNO is not null and to_char(DATE_OF_BIRTH, 'mm') = '03' and gender = 'W'
order by MEMBER_ID asc