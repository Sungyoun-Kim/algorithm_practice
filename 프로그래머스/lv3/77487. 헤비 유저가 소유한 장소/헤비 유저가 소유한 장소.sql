-- 코드를 입력하세요
select * from places where HOST_ID IN (select HOST_ID from (select *, count(*) as FREQ from  PLACES GROUP BY HOST_ID ) A  where A.FREQ >=2)