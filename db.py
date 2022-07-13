import sqlite3
class database:
      def __init__(self,db):
          self.con = sqlite3.connect(db)
          self.cur = self.con.cursor()
          sql = """
          CREATE TABLE IF NOT EXISTS employes(
          id integer Primary Key,
          name text,
          age text,
          job text,
          gender text,
          phone text,
          location text
          )
          """
          self.cur.execute(sql)
          self.con.commit()
      def insert(self,name,age,job,phone,gender,location):
          self.cur.execute("insert into employes values (NULL,?,?,?,?,?,?)",(name,age,job,phone,gender,location))
          self.con.commit()
      def fetch(self):
          self.cur.execute("SELECT * FROM employes")
          rows = self.cur.fetchall()
          return rows
      def remove(self,id):
          self.cur.execute("delete from employes where id=?",(id,))
          self.cur.commit()
      def update(self,name,age,job,phone,gender,location):
          self.cur.execute("update employes set name=?,age=?,job=?,phone=?,gender=?,location=? where id=?",(name,age,job,phone,gender,location,id))
          self.cur.commit()