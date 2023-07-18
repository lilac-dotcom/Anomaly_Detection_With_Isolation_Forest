USE [UATO3UtilityDB]
select Var_Id, Result_On, CAST(Result AS FLOAT) AS Result
from Execution
where Var_Id = 341 and Result > 1900.00 