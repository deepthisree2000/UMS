import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='deepthi@2000'
)
cur=conn.cursor()

class read:
    def deptread(x,colname,value):
        cur.execute(f"select * from department where {colname}='{value}'")
        print(cur.fetchall())
    def courseread(x,colname,value):
        cur.execute(f"select * from course where {colname}='{value}'")
        print(cur.fetchall())
    def facultyread(x,colname,value):
        cur.execute(f"select * from faculty where {colname}='{value}'")
        print(cur.fetchall())
    def studentread(x,colname,value):
        cur.execute(f"select * from student where {colname}='{value}'")
        print(cur.fetchall())
    

        