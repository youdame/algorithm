-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, TO_CHAR(HIRE_YMD, 'yyyy-mm-dd') 
from DOCTOR
where MCDP_CD = 'CS' or MCDP_CD = 'GS'
order by HIRE_YMD desc, dr_name asc

 -- TO_CHAR(HIRE_YMD, 'yyyy-mm-dd')