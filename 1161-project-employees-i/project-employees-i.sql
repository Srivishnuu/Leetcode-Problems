# Write your MySQL query statement below
Select P.project_id,ROUND(AVG(E.experience_years),2) AS average_years
from Project P join Employee E
on p.employee_id = E.employee_id
group by P.project_id
