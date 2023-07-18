USE [UATO3UtilityDB]
SELECT MAX(CAST(Result AS INT)) AS MaxResult
FROM Execution
WHERE Var_Id = 299;