import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='deepthi@2000'
)
cur=conn.cursor()

class insert:
    def deptinsert(x,deptid,deptname):
        cur.execute(f"insert into department values({deptid},'{deptname}')")
        conn.commit()
        print("Data has been inserted successfully")
    def courseinsert(x,courseid,coursename,coursefee,duration):
        cur.execute(f"insert into course values({courseid},'{coursename}',{coursefee},{duration})")
        conn.commit()
        print("Data has been inserted successfully")
    def facultyinsert(x,facultyid,facultyname,deptid,salary,courseid):
        cur.execute(f"insert into faculty values({facultyid},'{facultyname}',{deptid},{salary},{courseid})")
        conn.commit()
        print("Data has been inserted successfully")
    def studentinsert(x,sid,sname,courseid,departmentid):
        cur.execute(f"insert into student values({sid},'{sname}',{courseid},{departmentid})")
        conn.commit()
        print("Data has been inserted successfully")



    