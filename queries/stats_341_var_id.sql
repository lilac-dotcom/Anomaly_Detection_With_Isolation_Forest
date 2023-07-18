USE [UATO3UtilityDB]
SELECT MAX(CAST( [Result] AS FLOAT)) as MaxResult, AVG(CAST( [Result] AS FLOAT)) as AvgResult, MIN(CAST( [Result] AS FLOAT)) as MinResult
FROM Execution
WHERE Var_Id = 341;