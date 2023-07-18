USE [UATO3UtilityDB]
SELECT Var_Id, COUNT(*) as count
FROM Execution
GROUP BY Var_Id;