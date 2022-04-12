import time

import mysql.connector

elements = [(i / 10) for i in range(11)]
print(elements)

mydb = mysql.connector.connect(
    host="localhost",
    port='3309',
    user="root",
    password="",
    database="selfduality"
)

mycursor = mydb.cursor()
sql = "INSERT INTO normal (a,b,c,d,e) VALUES (%s, %s,%s, %s,%s);"
sql2 = "INSERT INTO reversed (a,b,c,d,e) VALUES (%s, %s,%s, %s,%s);"

list = []
for a in elements:
    start = time.time()
    for b in elements:
        for c in elements:
            for d in elements:
                for e in elements:
                    row = [a, b, c, d, e]
                    sorte = sorted(row)
                    if row == sorte:
                        row_rev = [round((1 - a), 2), round((1 - b), 2), round((1 - c), 2), round((1 - d), 2),
                                   round((1 - e), 2)]
                        mycursor.execute(sql, tuple(row))
                        mydb.commit()
                        mycursor.execute(sql2, tuple(row_rev))
                        mydb.commit()
    stop = time.time()
    print(stop - start)
mycursor.close()
mydb.close()
