create database UMS;
show databases;
use ums;
Create table department 
( departmentid int primary key,
  departmentname varchar(50));
Create table course 
( courseid int primary key,
  coursename varchar(45),
  coursefee int,
  duration int );  
  Create table faculty
( facultyid int primary key,
  facultyname varchar(45),
  departmentid int,
  salary int,
  courseid int,
   foreign key (courseid) references course(courseid));
Create table student
( sid int primary key,
  sname varchar(30),
  courseid int,
  departmentid int,
  foreign key (courseid) references course(courseid),
  foreign key (departmentid) references department(departmentid));

show tables;
