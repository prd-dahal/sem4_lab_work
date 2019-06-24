use lab2;
show tables;
desc employees;
desc offices;
desc customers;
desc orderdetails;
desc orders;
select * from orders where status='Shipped';
desc orderdetails;
-- 1. Find the product name and product vendor information for orders made by customer number 103.
select p.productName,p.productVendor from products p, orderdetails od,customers c,orders o where p.productCode=od.productCode and o.customerNumber=c.customerNumber and o.orderNumber=od.orderNumber and c.customerNumber=103; 
-- 2. Find the name of customers who ordered items between ‘2003-10-01’ and ‘2003-10-30’ and status of item is ‘Shipped’.
select c.customerName from orders o, customers c where o.customerNumber=c.customerNumber and o.status='shipped' and o.orderDate between '2003-10-01' and '2003-10-30';
-- 3. Find the customer name and credit limit of the customers who made orders with order numbers
-- in 10128, 10130, 10136, 10137.
select c.customerName, c.creditLimit from customers c, orders o where c.customerNumber=o.customerNumber and (o.orderNumber=10128 or o.orderNumber=10130 or o.orderNumber=10136 or o.orderNumber=10137);
-- 4. List the name of employees who are located at ‘Sydney’ Office.
select concat(e.firstName," ",e.lastName) from employees e ,offices o where e.officeCode=o.officeCode and o.city='Sydney';
-- 5. List all the product details for the orders made by Diego Freyre ( contactFirstName
-- contactLastName).
select od.* from orderdetails od, orders o, customers c where od.orderNumber=o.orderNumber and o.customerNumber=c.customerNumber and contactFirstName='Diego' and contactLastName='Freyre';
-- Nested Queries
-- 6. List firstName, lastName and email of employee who is located in office at ‘San Francisco’.
select firstName,lastName, email from employees where officeCode=(select officeCode from offices where city='San Francisco');
-- 7. Find the details of employees who reports to ‘Diane Murphy’.
select * from employees where reportsTo = (select employeeNumber from employees where lastName='Murphy');
-- 8. Find the product name and productline that are contained in order number 10100.
select productName, productLine from products where productCode in (select productCode from orderdetails where orderNumber=10100);