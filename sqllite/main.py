import sqlite3


def printvalue(s):
    print(s)
    return None


"""
 do.execute(\"\"\"CREATE TABLE customer(
       first_name text,
       last_name text,
       email text)
       \"\"\")
       """


def dsa():
    do.execute("""INSERT INTO customer VALUES(
        'alsdaadddi',
    'doe',
    'john_doe@hotmail.com'
     )
     """)


if __name__ == '__main__':
    con = sqlite3.connect("db.db")
    do = con.cursor()
    dsa()
    dsa()
    list = do.execute("""SELECT * FROM CUSTOMER""")
    print(len(list.fetchall()))
    # for item in list:
    #   print(item)
    do.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='customer'")
    print(do.fetchall())

    con.commit()
    con.close()
