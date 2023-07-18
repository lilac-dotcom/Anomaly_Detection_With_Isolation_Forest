USE [UATO3UtilityDB]
select count(*)
from Execution
where Var_Id = 340 and CAST( [Result] AS FLOAT) between 10 and 20

-- select count(*)
-- from Execution
-- where Var_Id = 340 and CAST( [Result] AS FLOAT) between 1900 and 2000