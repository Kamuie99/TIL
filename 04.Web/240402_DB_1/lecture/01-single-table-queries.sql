------------------------ 01. Querying data --------------------------
-- 테이블 employees에서 LastName 필드의 모든 데이터를 조회
SELECT LastName FROM employees;

-- 테이블 employees에서 LastName, FirstName 필드의 모든 데이터를 조회
SELECT LastName, FirstName FROM employees;

-- 테이블 employees에서 모든 필드 데이터를 조회
SELECT * FROM employees;

-- 테이블 employees에서 FirstName 필드의 모든 데이터를 조회
-- (단, 조회 시 FirstName이 아닌 '이름'으로 출력)
SELECT FirstName AS '이름' FROM employees;

-- 테이블 tracks에서 Name, Milliseconds 필드의 모든 데이터 조회
-- (단, Milliseconds 필드는 60000으로 나눠 분 단위 값으로 출력)
SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks;

------------------------ 02. Sorting data ------------------------
-- 테이블 employees에서 FirstName 필드의 모든 데이터를 오름차순 조회
SELECT FirstName from employees ORDER BY FirstName;

-- 테이블 employees에서 FirstName 필드의 모든 데이터를 내림차순 조회
SELECT FirstName FROM employees ORDER BY FirstName DESC;

-- 테이블 customers에서 Country 필드를 기준으로 내림차순 정렬한 다음
-- City 필드 기준으로 오름차순 정렬하여 조회
SELECT Country, City FROM customers ORDER BY Country DESC, City;

-- 테이블 tracks에서 Milliseconds 필드를 기준으로 내림차순 정렬한 다음
-- Name, Milliseconds 필드의 모든 데이터를 조회
-- (단, Milliseconds 필드는 60,000 으로 나눠 분 단위 값으로 출력)
SELECT 
  Name, Milliseconds / 60000 AS '재생 시간(분)' 
FROM 
  tracks 
ORDER BY
  Milliseconds DESC;

------------------------ NULL 정렬 예시 ------------------------
SELECT ReportsTo FROM employees ORDER BY ReportsTo;

------------------------ 03. Filtering data ------------------------
-- 테이블 customers에서 Country 필드의 모든 데이터를 오름차순 조회
SELECT Country FROM customers ORDER BY Country;

-- 테이블 customers에서 Country 필드의 모든 데이터를 중복 없이 오름차순 조회
SELECT DISTINCT Country FROM customers ORDER BY Country;

-- 테이블 customers에서 City 필드값이 Prague인 데이터의 LastName, FirstName, City 조회
SELECT LastName, FirstName, City FROM customers WHERE City='Prague';

-- 테이블 customers에서 City 필드값이 Prague가 아닌 데이터의 LastName, FirstName, City 조회
SELECT LastName, FirstName, City FROM customers WHERE City != 'Prague';

-- 테이블 customers에서 Company 필드 값이 NULL이고 Country 필드 값이 'USA'인 데이터의
-- LastName, FirstName, Company, Country 조회
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company IS NULL AND Country = 'USA';

-- 테이블 customers에서 Company 필드 값이 NULL이거나 Country 필드 값이 'USA'인 데이터의
-- LastName, FirstName, Company, Country 조회
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company IS NULL OR Country = 'USA';

-- 테이블 tracks에서 Bytes 필드 값이 10,000 이상 500,000 이하인 데이터의 Name, Bytes 조회
SELECT Name, Bytes FROM tracks WHERE Bytes >= 10000 AND Bytes <= 500000;
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 10000 AND 500000;

-- 테이블 tracks에서 Bytes 필드 값이 10,000 이상 500,000 이하인 데이터의 
-- Name, Bytes를 Bytes 기준으로 오름차순 조회
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 10000 AND 500000 ORDER BY Bytes;

-- 테이블 customers에서 Country 필드 값이 'Canada' 또는 'Germany' 또는 'France'인 데이터의
-- LastName, FirstName, Country 조회
SELECT LastName, FirstName, Country FROM customers WHERE Country IN ('Canada', 'Germany', 'France');

-- 테이블 customers에서 Country 필드 값이 'Canada' 또는 'Germany' 또는 'France'가 아닌 데이터의
-- LastName, FirstName, Country 조회
SELECT LastName, FirstName, Country FROM customers WHERE Country NOT IN ('Canada', 'Germany', 'France');

-- 테이블 customers에서 LastName 필드 값이 'son'으로 끝나는 데이터의 LastName, FirstName 조회
SELECT LastName, FirstName FROM customers WHERE LastName LIKE '%son';

-- 테이블 customers에서 FirstName 필드 값이 4자리면서 'a'로 끝나는 데이터의 LastName, FirstName 조회
SELECT LastName, FirstName FROM customers WHERE FirstName LIKE '___a';

-- 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 7개만 조회
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 7;

-- 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 
-- 기준 내림차순으로 4번째부터 7번째 데이터만 조회
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 3, 4;

-- 04. Grouping data
SELECT Country, COUNT(*) FROM customers GROUP BY Country;

-- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
SELECT Composer, AVG(Bytes) FROM tracks GROUP BY Composer ORDER BY AVG(Bytes) DESC;

-- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10 미만인
-- 데이터 조회(단, Milliseconds 필드는 60,000으로 나눠 분 단위 값의 평균으로 계산)
SELECT 
  Composer, 
  AVG(Milliseconds/60000) AS avgOfMinute 
FROM 
  tracks
GROUP BY 
  Composer
HAVING
  avgOfMinute < 10;