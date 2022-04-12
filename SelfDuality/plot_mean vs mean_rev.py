import matplotlib.pyplot as plt
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port='3309',
    user="root",
    password="",
    database="selfduality"
)
mycursor = mydb.cursor()

table_name = 'a1'

mycursor.execute("select mean, mean_rev from "+table_name)
data = mycursor.fetchall()
print(data)
mean = [x[0] for x in data]
mean_rev = [(1-x[1]) for x in data]

ind = [x for x, _ in enumerate(mean)]
print(data)

plt.rcParams["figure.figsize"] = (20,3)

plt.bar(ind, mean, color='red')
plt.bar(ind, mean_rev, color='gold')
plt.ylabel('mean vs mean_rev.py')

plt.savefig('mean_vs_mean_'+table_name+'.png', dpi=300)
plt.show()
