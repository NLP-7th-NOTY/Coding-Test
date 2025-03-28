 WITH ECOLI_CTE (ID, PARENT_ID, Generation) AS ( -- 이거 () 안에 굳이 칼럼 명 쓰지 않아도 됨. 가독성 용도임
    -- 1세대 (최초 개체)
    SELECT 
        ID, 
        PARENT_ID, 
        1 AS Generation
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 재귀적으로 자식 개체 탐색
    SELECT 
        E.ID, 
        E.PARENT_ID, 
        C.Generation + 1
    FROM ECOLI_DATA E
    INNER JOIN ECOLI_CTE C ON E.PARENT_ID = C.ID
)
-- 3세대 개체 필터링 및 정렬
SELECT ID
FROM ECOLI_CTE
WHERE Generation = 3
ORDER BY ID;