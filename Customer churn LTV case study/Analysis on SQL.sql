-- Active: 1678809478574@@127.0.0.1@3306@churn
SELECT Gender, COUNT(`Gender`) as COUNT
FROM customer
GROUP BY Gender;
-- its balanced


SELECT Partner, COUNT(Partner) as COUNT
FROM customer
GROUP BY Partner;
-- its balanced


SELECT Dependents, COUNT(Dependents) as COUNT
FROM customer
GROUP BY Dependents;
-- 23% have dependants



SELECT ROUND(AVG(Tenure),2) FROM cust_account;
-- average tenure is 32 monthS


SELECT ROUND(AVG(`TotalCharges`),2) FROM cust_account;
-- average `TotalCharges` is 2281$


SELECT ROUND(AVG(`MonthlyCharges`),2) FROM cust_account;


SELECT COUNT(*) FROM cust_account
WHERE `TotalCharges`>
(SELECT AVG(`TotalCharges`) FROM cust_account);


SELECT COUNT(*) FROM cust_account
WHERE `TotalCharges`<
(SELECT AVG(`TotalCharges`) FROM cust_account);

-- 2648 customers spends more than average of total charges
SELECT Churn,COUNT(`Churn`) 
FROM cust_churn
GROUP BY `Churn`;

SELECT c.Churn, avg(a.TotalCharges)
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`;
--- non churners paid a huge amount than non churners more than 1000$ difference


SELECT c.Churn, avg(a.`MonthlyCharges`)
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`;
--- interestingly, churners pay more monthly charges than non churners, we can dive deep into that.


SELECT c.Churn,a.`Contract`, COUNT(a.`Tenure`) as 'contract count'
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`,a.`Contract`;
--- yearly contracts influence customers to stay


SELECT c.Churn, COUNT(a.`Account_id`),
CASE WHEN `MonthlyCharges`>
(SELECT AVG(`MonthlyCharges`) FROM cust_account) THEN 'High_payers'
WHEN `MonthlyCharges`<=
(SELECT AVG(`MonthlyCharges`) FROM cust_account) THEN 'low_payers'
END AS 'Category'
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`, Category;
-- Major proportion of Churners are High payers

-- This alone can't give conclusion, we must continue the analysis in python

