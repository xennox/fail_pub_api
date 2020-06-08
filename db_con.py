import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

#Edit db
def edit(query):
    c.execute(query)
    conn.commit()

#Get data from db
def select(query):
    c.execute(query)
    return c.fetchall()

def Get_Lenght(query):
    result=c.execute(query)
    if len(c.fetchall())>0:
        return True
    else:
        return False