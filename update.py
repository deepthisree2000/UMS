import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='deepthi@2000'
)
cur=conn.cursor()

class update:
    def deptupdate(x,colname,ndeptname,odeptname):
        cur.execute(f"update department set {colname}='{ndeptname}' where {colname}='{odeptname}'")
        conn.commit()
        print("Data has been updated successfully.")
    def courseupdate(x,colname,newvalue,oldvalue):
        cur.execute(f"update course set {colname}={newvalue} where {colname}={oldvalue}")
        conn.commit()
        print("Data has been updated successfully")
    def facultyupdate(x,colname,newval,oldval):
        cur.execute(f"update faculty set {colname}='{newval}' where {colname}='{oldval}'")
        conn.commit()
        print("Data has been updated successfully")
    def studentupdate(x,colname,newone,oldone):
        cur.execute(f"update student set {colname}='{newone}' where {colname}='{oldone}'")
        conn.commit()
        print("Data has been updated successfully")
       

