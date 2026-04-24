
WITH CAL_GRADE as (SELECT EMP_NO, (
    CASE 
    WHEN AVG(SCORE) >= 96 THEN 'S'
    WHEN AVG(SCORE) >= 90 THEN 'A'
    WHEN AVG(SCORE) >= 80 THEN 'B'
    ELSE 'C'
    END
    ) as GRADE
FROM HR_GRADE
GROUP BY EMP_NO)


SELECT E.EMP_NO, EMP_NAME, GRADE, (CASE 
                                   WHEN GRADE = 'S' THEN SAL * 0.2
                                   WHEN GRADE = 'A' THEN SAL * 0.15
                                   WHEN GRADE = 'B' THEN SAL * 0.1
                                   ELSE SAL * 0
                                   END) as SAL
                                   
FROM HR_EMPLOYEES E 
JOIN CAL_GRADE G
ON E.EMP_NO = G.EMP_NO
ORDER BY EMP_NO
