USE [UATO3UtilityDB]
SELECT Var_Id, Result, COUNT(*) as count
FROM Execution
WHERE Var_Id IN (340)
GROUP BY Var_Id, Result