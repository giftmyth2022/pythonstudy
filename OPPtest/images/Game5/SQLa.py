import pandas as pa
import sqlite3 as sq

def check(db_name,table_name):
    conn = sq.connect(db_name)
    cursor = conn.cursor()
    sql = '''select tbl_name From sqlite_master where type = 'table' '''
    cursor.execute(sql)
    values = cursor.fetchall()
    tables = []
    for v in values:
        tables.append(v[0])
    if table_name not in tables:
        return False
    else:
        return True

def adddata_channel(dbname,name,age):
    conn = sq.connect(dbname)
    cur = conn.cursor()
    sql = 'INSERT INTO D_channel (name,age) values (?,?)'
    data = [name,age]
    cur.execute(sql,data)
    conn.commit()
    cur.close()
    conn.close()

def selectData_dchannel():
    conn = sq.connect('test.db')
    cur = conn.cursor()
    sql = "select * from D_channel"
    print(cur.execute(sql).fetchall())
    return cur.execute(sql).fetchall()

arr = selectData_dchannel()

print(list(arr[1]))
