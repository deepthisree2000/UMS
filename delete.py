import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='deepthi@2000'
)
cur=conn.cursor()

class delete:
    def deptdelete(x,id):
        cur.execute(f"delete from department where departmentid={id}")
        conn.commit()
        print("Data has been deleted successfully")
    def coursedelete(x,id):
        cur.execute(f"delete from course where courseid={id}")
        conn.commit()
        print("Data has been deleted successfully.")
    def facultydelete(x,id):
        cur.execute(f"Delete from faculty where facultyid={id}")
        conn.commit()
        print("Data has been deleted successfully.")
    def studentdelete(x,id):
        cur.execute(f"delete from student where studentid={id}")
        conn.commit()
        print("Data has been deleted successfully.")
        
