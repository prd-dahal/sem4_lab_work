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
-- creating datbase department
create table Department(
	DID smallint,
    DName varchar(20),
    Email varchar(20)
);
-- adding foreign key
alter table employee 
add foreign key(EID) references Department(DID);
show tables;
desc employee;
-- Q no 6 creating table with foreign key ONo 
create table customers(
	CID smallint primary key,
    CName varchar(25),
    Caddress varchar(25),
    CphoneNo bigint,
    ONo smallint,
    foreign key(ONo) references Orders(ONo)
    
);
-- orders table 
create table Orders(
	ONo smallint primary key,
    NoOfPiece int,
    DeliveryTime datetime
);
drop table Orders;
desc Orders;
show tables;