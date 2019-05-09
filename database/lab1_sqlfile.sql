-- create a database
create database if not exists SXC;
-- use databasee sxc
use SXC;
-- create table employee
create table employee(
	EID int,
    FirstName varchar(15),
    LastName varchar(15),
    DeptId smallint,
    DOB date
);
-- add contact no, salary in table
alter table employee 
	add column (ContactNo bigint, Salary decimal(10,2));
-- delete DOB column in the table
alter table employee 
	drop column DOB;

desc employee;
