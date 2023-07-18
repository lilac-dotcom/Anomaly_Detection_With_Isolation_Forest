USE [UATO3UtilityDB]
SELECT Var_Id, CAST( [Result] AS FLOAT) AS Result, COUNT(*) as count
FROM Execution
WHERE Var_Id IN (341)
GROUP BY Var_Id, Result
ORDER BY Result ASC;