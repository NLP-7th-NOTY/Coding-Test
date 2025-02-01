-- 틀린 쿼리 (TO_DATE와 문자열을 비교해버림;;)
SELECT MCDP_CD , COUNT(APNT_NO)
FROM APPOINTMENT
WHERE TO_DATE(APNT_YMD, 'YYYY-MM') = '2022-05'
GROUP BY MCDP_CD;

-- 정답 쿼리 (날짜 비교는 범위 조건을 사용해야함 BETWEEN 또는 >= AND <) + alias 문자열로할때는 쌍따옴표 또는 생략 (홑따옴표 아님)
-- 쌍 따옴표를 쓰면 대소문자 구분되므로 주의
SELECT MCDP_CD AS "진료과코드" , COUNT(APNT_NO) AS "5월예약건수"
FROM APPOINTMENT
WHERE APNT_YMD >= TO_DATE('2022-05-01', 'YYYY-MM-DD') AND APNT_YMD < TO_DATE('2022-06-01', 'YYYY-MM-DD')
GROUP BY MCDP_CD
ORDER BY "5월예약건수", "진료과코드";

-- 더 좋은 쿼리 (TRUNC 사용)
SELECT MCDP_CD AS "진료과코드" , COUNT(APNT_NO) AS "5월예약건수"
FROM APPOINTMENT
WHERE TRUNC(APNT_YMD, 'MM') = TO_DATE('2022-05', 'YYYY-MM')
GROUP BY MCDP_CD
ORDER BY "5월예약건수", "진료과코드";