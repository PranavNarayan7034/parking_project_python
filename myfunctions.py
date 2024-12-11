import mysql.connector as m

def myconnection():
    c = m.connect(host='localhost',user='root',password='root',database='parking')
    return c

def insertdata(tablename,vn,d1,d2):
    sc = myconnection()
    c = sc.cursor()
    c.execute(f'''insert into {tablename} values("{vn}","{d1}","{d2}")''')
    sc.commit()
    c.close()
    sc.close()