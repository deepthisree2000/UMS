
from tabulate import tabulate
from insert import insert
from update import update
from delete import delete
from read import read
obj=insert()
obj1=update()
obj2=delete()
obj3=read()
print("Welcome to the University Management System!")
print("\n Database Information:")
print("It has following tables:")
print(tabulate({'Department': ['Departmentid', 'Departmentname'], 
                'Course': ['Courseid', 'Coursename', 'Coursefee','Duration'], 
                'Faculty': ['Facultyid','Facultyname','departmentid','salary','courseid'],
                'Student':['Sid','Sname','Courseid','Departmentid']}, 
                headers='keys', 
                tablefmt='outline',
                missingval="--"))
print("-------------------------------------------------------------------------")

print("Operations that can be performed on database are : \n 1.add\n 2.update\n 3.delete\n 4.read ")
opr=input("Enter operation you want to perform: ")
if opr=='add':
    print(" For adding data into department table type:'a'\n For addind data into course table type:'b'\n For adding data into faculty table type:'c'\n For adding data into student table type:'d' ")
    
    tab=input("Enter the table name:  ")
    if tab=='a':
        deptid=int(input("Enter deptid: "))
        deptname=input("Enter deptname: ")
        obj.deptinsert(deptid,deptname)
    if tab=='b':
        courseid=int(input("Enter courseid: "))
        coursename=input("Enter coursename: ")
        coursefee=int(input("Enter fee: "))
        duration=int(input("Enter duration of course: "))
        obj.courseinsert(courseid,coursename,coursefee,duration)
    if tab=='c':
        facultyid=int(input("Enter id:"))
        facultyname=input("Enter name: ")
        deptid=int(input("Enter deptid: "))
        salary=int(input("Enter salary: "))
        courseid=int(input("Enter courseid: "))
        obj.facultyinsert(facultyid,facultyname,deptid,salary,courseid)
    if tab=='d':
        sid=int(input("Enter id: "))
        sname=input("Enter name: ")
        courseid=int(input("Enter courseid: "))
        departmentid=int(input("Enter departmentid: "))
        obj.studentinsert(sid,sname,courseid,departmentid)


if opr=='update':
    print(" To update department table press - 1\n To update course table press-2\n To update faculty table press- 3\n To update student table press - 4")
    tab=int(input("Enter the number to update "))
    if tab==1:
        colname=input("Enter the column name ")
        ndeptname=input("Enter new value ")
        odeptname=input("Enter old value ")
        obj1.deptupdate(colname,ndeptname,odeptname)
    if tab==2:
        colname=input("enter the column name: ")
        oldvalue=input("Enter the old value:")
        newvalue=input("enter the new value:")
        obj1.courseupdate(colname,newvalue,oldvalue)
    if tab==3:
        colname=input("Enter colname to update:")
        newval=input("Enter new value: ")
        oldval=input("enter old value: ")
        obj1.facultyupdate(colname,newval,oldval)
    if tab==4:
        colname=input("enter colname to update: ")
        newone=input("Enter new value: ")
        oldone=input("Enter old value: ")
        obj1.studentupdate(colname,newone,oldone)


if opr=='delete':
    print(" To delete from department table press - 1\n To delete from course table press - 2\n To delete from faculty table press - 3\n To delete from student table press -4")
    tab=int(input("Enter table number to delete "))
    if tab==1 :
        id=input("Enter id ")
        obj2.deptdelete(id)
    if tab==2:
        id=int(input("Enter courseid to delete:  "))
        obj2.coursedelete(id)
    if tab==3:
        id=int(input("Enter facultyid to delete:  "))
        obj2.facultydelete(id)
    if tab==4:
        id=int(input("Enter studentid to delete:  "))
        obj2.studentdelete(id)

if opr=='read':
    
    tab=input(" Enter 'a' to read department table\n Enter 'b' to read course table\n Enter 'c' to read faculty table\n Enter 'd' to read student table. ")
    if tab=='a':
        colname=input("Enter column name: ")
        value=input("Enter value of column: ")
        obj3.deptread(colname,value)
    if tab=='b':
        colname=input("Enter column name: ")
        value=input("Enter value")
        obj3.courseread(colname,value)
    if tab=='c':
        colname=input("Enter column name: ")
        value=input("Enter value: ")
        obj3.facultyread(colname,value)
    if tab=='d':
        colname=input("Enter column name: ")
        value=input("Enter value:  ")
        obj3.studentread(colname,value)

    

