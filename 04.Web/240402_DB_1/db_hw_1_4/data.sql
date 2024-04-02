-- 1. name의 값에 love 글자를 포함한 데이터를 조회하시오.
SELECT * FROM tracks WHERE name LIKE '%love%';

-- 2. GenreId의 값이 1이고, Milliseconds의 값이 300000 이상인
-- 데이터를 모두 조회하여 UnitPrice 기준으로 내림차순 정렬하여 조회
SELECT * FROM tracks WHERE GenreId=1 and Milliseconds >=300000 ORDER BY UnitPrice DESC;

-- 3. GenreId 별로 그룹화 하여, GenreId와 각 그룹별 데이터의 수를 조회하시오.
-- 단, 그룹별 데이터 수는 TotalTracks 필드로 표기하여 나타내시오.
SELECT
  GenreId, COUNT(*) AS TotalTracks
FROM
  tracks
GROUP BY
  GenreId;

-- 4. GenreId별로 그룹화 하여, GenreId와 각 그룹별 UnitPrice의 총 합을 계산하여 
-- 조회하시오. 단, UnitPrice의 총합은 TotalPrice로 표기하며, 그 중, TotalPrice의 
-- 값이 100 이상인 데이터들만 조회하시오.
SELECT
  GenreId, SUM(UnitPrice) AS TotalPrice
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;
