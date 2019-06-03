use lab2;

-- Q no 1 Find information of all employee whose extension starts with ‘x2’ and employee number between 1200 and 1500. (Employees table)

select * from employees where extension like 'x2%' and employeeNumber between 1200 and 1500  ;
-- Q no 2 Find the sum of quantity in stock for different categories of productline from product table.

select sum(quantityInStock),productLine from products group by(productLine);
-- Q no 3 Determine the total number of orders for status (‘Cancelled’, ’Disputed’, ’In Process’, ’On Hold’). (order table) 
select count(orderNumber),status from orders group by (status) having status='Cancelled' or status='Disputed' or status='In Process' or status='On Hold';
-- Q no 4 Determine the number of employees as per the job title. (employees table)
select * from employees;
select count(employeeNumber),jobTitle from employees group by(jobTitle);
-- Q no 5 Find the customer numbers with sum of amount of payment is greater than 200000. (payments table) 
select * from payments;
select sum(amount), customerNumber from payments group by(customerNumber) having sum(amount)>200000;
-- List the name of cities where customer number is greater than 2. (customers table)
select * from customers;
select city from customers group by(city) having count(customerNumber)>2;