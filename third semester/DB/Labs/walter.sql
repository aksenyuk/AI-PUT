/* Lab 1 */
/* Task 1 */
SELECT * FROM departments;
/* Task 2 */
SELECT * FROM employees;
/* Tsk 3 */
SELECT surname, job, salary*12 from employees;
/* Task 4 */
SELECT surname, job, salary*12 as "monthly_pay" from employees;
/* Task 5 */
SELECT surname, job, salary + add_salary as "monthly_income" from employees;
SELECT surname, job, monthly_income from employees ORDER BY monthly_income;


