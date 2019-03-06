import sqlite3
from sqlite3 import Error
class Remdb:

    def __init__(self,db):
        try:
            self.conn=sqlite3.connect(db)
            self.cur=self.conn.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS remindme(id INTEGER PRIMARY KEY,event text ,descr text,date INTEGER, status text )")
            self.conn.commit()
        except Error as e:
            print(e)
            
        return None

    def insert(self,event,descr,date,status):
        self.cur.execute("INSERT into remindme VALUES (NULL,?,?,?,?)",(event,descr,date,status))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM remindme")
        rows=self.cur.fetchall()
        return rows

    def search(self,event="",descr="",date="",status=""):
        self.cur.execute("SELECT * FROM remindme where event=? OR descr=? OR date=? OR status=?",(event,descr,date,status))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM remindme where id =?",(id,))
        self.conn.commit()

    def update(self,id,event,descr,date,status):
        self.cur.execute("UPDATE remindme SET event=?,descr=?,date=?,status=? WHERE id=?",(event,descr,date,status,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
