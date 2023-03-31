-- Active: 1678809478574@@127.0.0.1@3306@churn
SELECT Gender, COUNT(`Gender`) as COUNT
FROM customer
GROUP BY Gender;

SELECT Partner, COUNT(Partner) as COUNT
FROM customer
GROUP BY Partner;

SELECT Dependents, COUNT(Dependents) as COUNT
FROM customer
GROUP BY Dependents;

SELECT ROUND(AVG(Tenure),2) FROM cust_account;
SELECT ROUND(AVG(`TotalCharges`),2) FROM cust_account;
SELECT ROUND(AVG(`MonthlyCharges`),2) FROM cust_account;
SELECT COUNT(*) FROM cust_account
WHERE `TotalCharges`>
(SELECT AVG(`TotalCharges`) FROM cust_account);
SELECT COUNT(*) FROM cust_account
WHERE `TotalCharges`<
(SELECT AVG(`TotalCharges`) FROM cust_account);
SELECT Churn,COUNT(`Churn`) 
FROM cust_churn
GROUP BY `Churn`;
SELECT c.Churn, avg(a.TotalCharges)
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`;
--- Churners paid a huge amount than non churners
SELECT c.Churn, avg(a.`MonthlyCharges`)
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`;
SELECT c.Churn,a.`Contract`, COUNT(a.`Tenure`) as 'contract count'
FROM cust_churn c
INNER JOIN cust_account a ON a.`Account_id` = c.`id`
GROUP BY c.`Churn`,a.`Contract`;
--- yearly contracts influence customers to stay
