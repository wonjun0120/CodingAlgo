-- 코드를 작성해주세요
with a as (
    select 
        max(SIZE_OF_COLONY) as max_size,
        YEAR(DIFFERENTIATION_DATE) as year
    from ECOLI_DATA 
    group by year
)
select 
    a.year as YEAR,
    a.max_size - ECOLI_DATA.SIZE_OF_COLONY as YEAR_DEV,
    ECOLI_DATA.ID
from a, ECOLI_DATA
where 
    YEAR(ECOLI_DATA.DIFFERENTIATION_DATE) = a.year
order by 
    YEAR, 
    YEAR_DEV